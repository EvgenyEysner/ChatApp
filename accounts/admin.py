from django.contrib import admin
from django.utils.html import format_html

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px;"/>'.format(obj.avatar.url))

    image_tag.short_description = 'аватар'
    list_display = ['username', 'image_tag']
