from django.contrib import admin
from django.utils.html import format_html

from .models import Room, Message


@admin.register(Message)
class MessageUserAdmin(admin.ModelAdmin):
    def file_tag(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px;"/>'.format(obj.file.url))

    date_hierarchy = 'timestamp'
    file_tag.short_description = 'файл'
    list_display = ['sender', 'receiver', 'message', 'timestamp', 'is_read', 'file_tag', 'is_private', 'room']


@admin.register(Room)
class RoomUserAdmin(admin.ModelAdmin):

    date_hierarchy = 'created'
    list_display = ['name']