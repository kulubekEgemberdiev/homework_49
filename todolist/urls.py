from django.urls import path

from todolist.views import Index

urlpatterns = [
    path("", Index.as_view(), name="index")
]