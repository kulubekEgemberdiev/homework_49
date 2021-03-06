# Generated by Django 4.0.6 on 2022-07-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuses',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterModelOptions(
            name='todolistmodel',
            options={'verbose_name': 'Todo', 'verbose_name_plural': 'Todo-List'},
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.AlterField(
            model_name='statuses',
            name='status',
            field=models.CharField(max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created date'),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todolist.statuses', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='summary',
            field=models.CharField(max_length=100, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todolist.types', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated date'),
        ),
        migrations.AlterField(
            model_name='types',
            name='type',
            field=models.CharField(max_length=50, verbose_name='Type'),
        ),
    ]
