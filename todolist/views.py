from audioop import reverse

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, FormView

# Create your views here.
from todolist.form import TodoForm, SearchForm
from todolist.models import TodolistModel


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        search_form = SearchForm(data=request.GET)
        todolist = TodolistModel.objects.all()
        if search_form.is_valid():
            search = search_form.cleaned_data.get("search_field")
            if search:
                todolist = todolist.filter(id__contains=search)
        todolist = todolist.order_by("-created_date")
        context = {"todolist": todolist, "form": search_form}
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
            types = form.cleaned_data.get("types")
            status = form.cleaned_data.get("status")
            new_todo = TodolistModel.objects.create(summary=summary, description=description, status=status)
            new_todo.types.set(types)
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
                "types": self.todo.types,
                "status": self.todo.status
            })
            return render(request, "update.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TodoForm(data=request.POST)
        if form.is_valid():
            self.todo.summary = form.cleaned_data.get("summary")
            self.todo.description = form.cleaned_data.get("description")
            self.todo.types = form.cleaned_data.get("types")
            self.todo.status = form.cleaned_data.get("status")
            self.todo.save()
            return redirect("detail", pk=self.todo.pk)
        return render(request, "update.html", {"form": form})

# class UpdateView(FormView):
#     form_class = TodoForm
#     template_name = "update.html"
#
#     def dispatch(self, request, *args, **kwargs):
#         self.todo = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return reverse("article_view", kwargs={"pk": self.todo.pk})
#
#     # def get_initial(self):
#     #     initial = {}
#     #     for key in 'title', 'content', 'author':
#     #         initial[key] = getattr(self.article, key)
#     #     initial['tags'] = self.article.tags.all()
#     #     return initial
#     def get_form_kwargs(self):
#         form_kwargs = super().get_form_kwargs()
#         form_kwargs['instance'] = self.todo
#         return form_kwargs
#
#     def form_valid(self, form):
#         # tags = form.cleaned_data.pop('tags')
#         # Article.objects.filter(pk=self.article.pk).update(**form.cleaned_data)
#         # for key, value in form.cleaned_data.items():
#         #     setattr(self.article, key, value)
#         # self.article.save()
#         # self.article.tags.set(tags)
#         self.todo = form.save()
#         return super().form_valid(form)
#
#     def get_object(self):
#         return get_object_or_404(TodolistModel, pk=self.kwargs.get("pk"))
