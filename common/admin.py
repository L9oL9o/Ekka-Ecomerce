from django.contrib import admin
from django.contrib.admin import ModelAdmin

from common.models import SocialMediaUrls


@admin.register(SocialMediaUrls)
class SocialMediaUrlsAdmin(ModelAdmin):
    list_display = ('id', 'facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'whatsapp')
    list_display_links = ('id', 'facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'whatsapp')
