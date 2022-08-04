from django.urls import path

from todolist.views.todolist_views import Index, DetailView, DeleteView, CreateView, UpdateView
from todolist.views.project_views import ProjectIndexView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, \
    ProjectDeleteView

app_name = 'todolist'

urlpatterns = [
    path("todolist/", Index.as_view(), name="index"),
    path("todolist/<int:pk>/detail/", DetailView.as_view(), name="detail"),
    path("todolist/<int:pk>/delete/", DeleteView.as_view(), name="delete"),
    path("todolist/<int:pk>/update/", UpdateView.as_view(), name="update"),
    path("projects/<int:pk>/create/", CreateView.as_view(), name="create"),
    path("", ProjectIndexView.as_view(), name="project_index"),
    path("projects/<int:pk>/detail/", ProjectDetailView.as_view(), name="project_detail"),
    path("projects/create/new/", ProjectCreateView.as_view(), name="project_create"),
    path("projects/<int:pk>/update/", ProjectUpdateView.as_view(), name="project_update"),
    path("projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete")
]
