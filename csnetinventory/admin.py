from django.contrib import admin

from .models import InventoryItem


class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'room', 'brand', 'acquired')

admin.site.register(InventoryItem, InventoryItemAdmin)
