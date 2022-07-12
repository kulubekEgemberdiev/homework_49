from django import forms
from django.forms import widgets

from todolist.models import Types, Statuses

types = Types
statuses = Statuses


class TodoForm(forms.Form):
    summary = forms.CharField(max_length=100, label="Summary")
    description = forms.CharField(max_length=2000, required=False, label="Description",
                                  widget=widgets.Textarea(attrs={"cols": 50, "rows": 2}))
    type = forms.ModelChoiceField(queryset=types.objects.all(), label="Type")
    status = forms.ModelChoiceField(queryset=statuses.objects.all(), label="Status")


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=50, required=False, label="Search by todo number")
