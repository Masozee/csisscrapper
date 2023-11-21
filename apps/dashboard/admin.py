# admin.py

from django.contrib import admin
from .models import Category, Option, Dataname, DataValue

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'keterangan')

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'keterangan')

@admin.register(Dataname)
class DatanameAdmin(admin.ModelAdmin):
    list_display = ('title', 'periode', 'source', 'keterangan')

@admin.register(DataValue)
class DataValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'value')
