from django.urls import path

from todolist.views import Index, DetailView, DeleteView, CreateView, UpdateView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("/todolist/<int:pk>/detail/", DetailView.as_view(), name="detail"),
    path("/todolist/<int:pk>/delete/", DeleteView.as_view(), name="delete"),
    path("/todolist/<int:pk>/update/", UpdateView.as_view(), name="update"),
    path("/todolist/create/new/", CreateView.as_view(), name="create")
]