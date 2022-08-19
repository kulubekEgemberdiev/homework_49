from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy

from django.shortcuts import get_object_or_404
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.
from todolist.form import TodoForm, SearchForm
from todolist.models import TodolistModel, ProjectModel


class Index(ListView):
    model = TodolistModel
    template_name = "todolist/index.html"
    context_object_name = "todolist"
    ordering = "-id"
    paginate_by = 10
    paginate_orphans = 2

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({"search": self.search_value})
            context["search"] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]
        return None


class DetailView(TemplateView):
    template_name = "todolist/detail.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        todo = get_object_or_404(TodolistModel, pk=pk)
        kwargs["todo"] = todo
        return super().get_context_data(**kwargs)


class DeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "todolist/delete.html"
    model = TodolistModel
    context_object_name = 'todolist'
    success_url = reverse_lazy('todolist:project_index')

    def has_permission(self):
        return self.request.user.has_perm('todolist.delete_todolistmodel')


class CreateView(PermissionRequiredMixin, CreateView):
    form_class = TodoForm
    template_name = "todolist/create.html"

    def has_permission(self):
        return self.request.user.has_perm('todolist.add_todolistmodel')

    def form_valid(self, form):
        project = get_object_or_404(ProjectModel, pk=self.kwargs.get("pk"))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("todolist:project_detail", kwargs={"pk": self.object.project.pk})


class UpdateView(PermissionRequiredMixin, UpdateView):
    model = TodolistModel
    template_name = "todolist/update.html"
    form_class = TodoForm

    def has_permission(self):
        return self.request.user.has_perm('todolist.change_todolistmodel')

    def get_success_url(self):
        return reverse("todolist:detail", kwargs={"pk": self.object.pk})
