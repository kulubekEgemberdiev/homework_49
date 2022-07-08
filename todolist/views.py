from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
from todolist.models import TodolistModel


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        todolist = TodolistModel.objects.order_by("id")
        context = {"todolist": todolist}
        return render(request, "index.html", context)


class DetailView(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        todo = get_object_or_404(TodolistModel, pk=pk)
        kwargs["todo"] = todo
        return super().get_context_data(**kwargs)


class DeleteView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        todo = get_object_or_404(TodolistModel, pk=pk)
        todo.delete()
        return redirect("index")
