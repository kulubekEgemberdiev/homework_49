from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
from todolist.form import TodoForm
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


class CreateView(View):
    def get(self, request, *args, **kwargs):
        form = TodoForm()
        return render(request, "create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TodoForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get("summary")
            description = form.cleaned_data.get("description")
            type = form.cleaned_data.get("type")
            status = form.cleaned_data.get("type")
            new_todo = TodolistModel.objects.create(summary=summary, description=description, type=type, status=status)
            return redirect("detail", pk=new_todo.pk)
        return render(request, "create.html", {"form": form})


class UpdateView(View):
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.todo = get_object_or_404(TodolistModel, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = TodoForm(initial={
                "summary": self.todo.summary,
                "description": self.todo.description,
                "type": self.todo.type,
                "status": self.todo.status
            })
            return render(request, "update.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TodoForm(data=request.POST)
        if form.is_valid():
            self.todo.summary = form.cleaned_data.get("summary")
            self.todo.description = form.cleaned_data.get("description")
            self.todo.type = form.cleaned_data.get("type")
            self.todo.status = form.cleaned_data.get("status")
            self.todo.save()
            return redirect("detail", pk=self.todo.pk)
        return render(request, "update.html", {"form": form})
