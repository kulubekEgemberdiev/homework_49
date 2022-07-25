from django.urls import path

from todolist.views.todolist_views import Index, DetailView, DeleteView, CreateView, UpdateView
from todolist.views.project_views import ProjectIndex

urlpatterns = [
    path("todolist/", Index.as_view(), name="index"),
    path("todolist/<int:pk>/detail/", DetailView.as_view(), name="detail"),
    path("todolist/<int:pk>/delete/", DeleteView.as_view(), name="delete"),
    path("todolist/<int:pk>/update/", UpdateView.as_view(), name="update"),
    path("todolist/create/new/", CreateView.as_view(), name="create"),
    path("", ProjectIndex.as_view(), name="project_index")
]