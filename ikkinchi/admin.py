from django.contrib import admin
from .models import Salom1, Salom2, Salom3, Salom4, Salom5
# Register your models here.

class Salom1Admin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    search_fields = ['name', 'is_active']
    list_filter = ['name', 'is_active']

admin.site.register(Salom1, Salom1Admin)

class Salom2Admin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    search_fields = ['name', 'is_active']
    list_filter = ['name', 'is_active']

admin.site.register(Salom2, Salom2Admin)

class Salom3Admin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    search_fields = ['name', 'is_active']
    list_filter = ['name', 'is_active']

admin.site.register(Salom3, Salom3Admin)

class Salom4Admin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    search_fields = ['name', 'is_active']
    list_filter = ['name', 'is_active']

admin.site.register(Salom4, Salom4Admin)

class Salom5Admin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    search_fields = ['name', 'is_active']
    list_filter = ['name', 'is_active']

admin.site.register(Salom5, Salom5Admin)