from django.urls import path

from todolist.views import Index, DetailView, DeleteView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("/todolist/<int:pk>/detail/", DetailView.as_view(), name="detail"),
    path("/todolist/<int:pk>/delete/", DeleteView.as_view(), name="delete"),
]