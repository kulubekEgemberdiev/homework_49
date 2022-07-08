from django import forms
from django.forms import widgets

from todolist.models import Types, Statuses

types = Types.objects.all()
statuses = Statuses.objects.all()


class TodoForm(forms.Form):
    summary = forms.CharField(max_length=100, label="Заголовок")
    description = forms.CharField(max_length=2000, required=False, label="Описание",
                                  widget=widgets.Textarea(attrs={"cols": 50, "rows": 2}))
    type = forms.ModelChoiceField(queryset=types, label="Тип")
    status = forms.ModelChoiceField(queryset=statuses, label="Статус")


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=50, required=False, label="Поиск")
