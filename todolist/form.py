from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from todolist.models import TodolistModel


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodolistModel
        fields = ["summary", "description", "types", "status"]
        widgets = {
            "description": widgets.Textarea(attrs={"cols": 50, "rows": 2}),
            "types": widgets.CheckboxSelectMultiple,
        }

    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        if len(summary) > 30:
            raise ValidationError("The todo summary must be shorter than or equal to 30 characters!")
        if len(summary) <= 3:
            raise ValidationError("The todo summary must be more than 3 characters!")
        return summary

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) > 2000:
            raise ValidationError("The todo description must be shorter than or equal to 2000 characters!")
        return description

    def clean_types(self):
        types = self.cleaned_data.get("types")
        if not types:
            raise ValidationError("You must specify at least one type for this todo!")
        return types


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label="Search")
