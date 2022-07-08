from django.db import models


# Create your models here.

class TodolistModel(models.Model):
    summary = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    status = models.ForeignKey("todolist.Statuses", on_delete=models.PROTECT, verbose_name="Статус")
    type = models.ForeignKey("todolist.Types", on_delete=models.PROTECT, verbose_name="Тип")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return f"{self.id}. {self.summary}. {self.type}. {self.status}. {self.created_date}. {self.updated_date}"

    class Meta:
        db_table = "todolist"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Types(models.Model):
    type = models.CharField(max_length=50, verbose_name="Тип")

    def __str__(self):
        return f"{self.type}"

    class Meta:
        db_table = "types"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Statuses(models.Model):
    status = models.CharField(max_length=50, verbose_name="Статус")

    def __str__(self):
        return f"{self.status}"

    class Meta:
        db_table = "statuses"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
