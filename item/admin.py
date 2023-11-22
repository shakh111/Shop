from django.contrib import admin
from .models import Category, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['-id']
    search_fields = ['name']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['-id']
    search_fields = ['name']