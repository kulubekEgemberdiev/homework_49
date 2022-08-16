from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

# Create your views here.
from accounts.forms import UserCreationForm
from accounts.models import Profile


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
