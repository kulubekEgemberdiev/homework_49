from django import forms
from django.forms import widgets

from todolist.models import Types, Statuses


class TodoForm(forms.Form):
    summary = forms.CharField(max_length=100, label="Заголовок")
    description = forms.CharField(max_length=2000, required=False, label="Описание",
                                  widget=widgets.Textarea(attrs={"cols": 50, "rows": 2}))
    type = forms.ModelChoiceField(queryset=Types.objects.all(), label="Тип")
    status = forms.ModelChoiceField(queryset=Statuses.objects.all(), label="Статус")

