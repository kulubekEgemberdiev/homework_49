from django.db.models import Q
from django.urls import reverse

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.http import urlencode
from django.views import View
from django.views.generic import TemplateView, FormView, ListView

# Create your views here.
from todolist.form import TodoForm, SearchForm
from todolist.models import TodolistModel


class Index(ListView):
    model = TodolistModel
    template_name = "todolist/index.html"
    context_object_name = "todolist"
    ordering = "-updated_date"
    paginate_by = 10
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
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]
        return None


class DetailView(TemplateView):
    template_name = "todolist/detail.html"

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
        return render(request, "todolist/create.html", {"form": form})

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
        return render(request, "todolist/create.html", {"form": form})


class UpdateView(FormView):
    form_class = TodoForm
    template_name = "todolist/update.html"

    def dispatch(self, request, *args, **kwargs):
        self.todo = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("detail", kwargs={"pk": self.todo.pk})

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['instance'] = self.todo
        return form_kwargs

    def form_valid(self, form):
        self.todo = form.save()
        return super().form_valid(form)

    def get_object(self):
        return get_object_or_404(TodolistModel, pk=self.kwargs.get("pk"))
