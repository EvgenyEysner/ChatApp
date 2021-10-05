from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ['email']
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg', verbose_name='аватар')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователь чата'
        verbose_name_plural = 'пользователи чата'