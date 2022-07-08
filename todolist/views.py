from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
from todolist.models import TodolistModel


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        todolist = TodolistModel.objects.order_by("id")
        context = {"todolist": todolist}
        return render(request, "index.html", context)
