from django.contrib import admin
from .models import Room



@admin.register(Room)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'room_name',
        'room_slug',
    )
