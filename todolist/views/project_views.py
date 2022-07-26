from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
from todolist.form import SearchForm, ProjectForm
from todolist.models import ProjectModel, TodolistModel


class ProjectIndexView(ListView):
    model = ProjectModel
    template_name = "project/project_index.html"
    context_object_name = "projects"
    ordering = "-id"
    paginate_by = 8
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
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]
        return None


class ProjectDetailView(DetailView):
    template_name = "project/project_detail.html"
    model = ProjectModel
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todolist'] = self.object.todolist.order_by("-updated_date")
        return context


class ProjectCreateView(CreateView):
    form_class = ProjectForm
    template_name = "project/project_create.html"

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        form.save_m2m()
        return redirect("project_detail", pk=project.pk)
