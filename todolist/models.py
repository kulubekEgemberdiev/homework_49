from django.db import models


# Create your models here.

class TodolistModel(models.Model):
    summary = models.CharField(max_length=30, verbose_name="Summary")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Description")
    status = models.ForeignKey("todolist.Statuses", on_delete=models.PROTECT, verbose_name="Status")
    types = models.ManyToManyField("todolist.Types", related_name="todolist", blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    def __str__(self):
        return f"{self.id}. {self.summary}. {self.types}. {self.status}. {self.created_date}. {self.updated_date}"

    class Meta:
        db_table = "todolist"
        verbose_name = "Todo"
        verbose_name_plural = "Todo-List"


class Types(models.Model):
    types = models.CharField(max_length=50, verbose_name="Type")

    def __str__(self):
        return f"{self.types}"

    class Meta:
        db_table = "types"
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Statuses(models.Model):
    status = models.CharField(max_length=50, verbose_name="Status")

    def __str__(self):
        return f"{self.status}"

    class Meta:
        db_table = "statuses"
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
