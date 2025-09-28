from django.contrib import admin

from .models import FeedBack


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ("id", "quality", "attitude", "speed", "comment","anonymous")
    list_filter = ("anonymous", )