from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import CreateView, DetailView, ListView, UpdateView

# Create your views here.
from accounts.forms import UserCreationForm, UserChangeForm, ProfileChangeForm
from accounts.models import Profile
from todolist.form import SearchForm


class RegistrationView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('todolist:project_index')
        return next_url


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "profile.html"
    paginate_by = 8
    paginate_orphans = 1
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        paginator = Paginator(self.get_object().projects.all(),
                              self.paginate_by,
                              self.paginate_orphans)
        page_number = self.request.GET.get('page', 1)
        page_object = paginator.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context['page_obj'] = page_object
        context['projects'] = page_object.object_list
        context['is_paginated'] = page_object.has_other_pages()
        return context


class UsersListView(PermissionRequiredMixin, ListView):
    model = get_user_model()
    template_name = "user_list.html"
    ordering = "-id"
    paginate_by = 8
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form
        context["users"] = User.objects.all()
        if self.search_value:
            context["query"] = urlencode({"search": self.search_value})
            context["search"] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(username__icontains=self.search_value) | Q(first_name__icontains=self.search_value) | Q(
                last_name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]
        return None

    def has_permission(self):
        return self.request.user.has_perm('todolist.view_user')


class ProfileUpdateView(PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'profile_update.html'
    profile_form = ProfileChangeForm
    context_object_name = 'user_obf'


    def has_permission(self):
        return self.request.user.is_superuser or self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        if 'profile_form' not in contex:
            contex['profile_form'] = self.profile_form(instance=self.get_object().profile)
        return contex

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        profile_form = self.profile_form(instance=self.object.profile, data=request.POST, files=request.FILES)
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        form.save()
        profile_form.save()
        return redirect('accounts:profile', self.object.pk)

    def form_invalid(self, form, profile_form):
        return self.render_to_response(self.get_context_data(form=form, profile_form=profile_form))


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.request.user.pk})