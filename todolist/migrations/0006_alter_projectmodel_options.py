# Generated by Django 4.0.6 on 2022-08-12 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_projectmodel_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectmodel',
            options={'permissions': [('can_add_users_to_project', 'Can add users to Project'), ('can_delete_users_in_project', 'Can delete users in Project')], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
    ]
