# Generated by Django 4.0.6 on 2022-07-08 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'db_table': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='TodolistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todolist.statuses', verbose_name='Статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todolist.types', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'db_table': 'todolist',
            },
        ),
    ]
