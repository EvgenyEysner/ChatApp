from django.db import models
from django.conf import settings
from django.utils import timezone


class Room(models.Model):
    name = models.CharField('название комнаты', max_length=50, unique=True)
    room_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, verbose_name='комнаты')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания: ')

    def __str__(self):
        return f'{self.name}, {self.created}'

    class Meta:
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'
        ordering = ['-created']


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    file = models.FileField('добавить файл', upload_to='users/files', null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='chat_room')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_private = models.BooleanField('приватное сообщение', default=False)

    def __str__(self):
        return f'{self.sender}: {self.message}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['-timestamp']