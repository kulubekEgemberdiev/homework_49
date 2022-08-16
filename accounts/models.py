from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, verbose_name='Avatar')
    github = models.URLField(max_length=150, null=True, blank=True, verbose_name='Link to GitHub')
    about_info = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Yourself info')
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile', verbose_name='User')