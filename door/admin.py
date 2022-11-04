from django.contrib import admin
from .models import *



class InterfaceAdminUser(admin.ModelAdmin):
    list_display = ('name', 'login','door_id', 'photo', 'time_created', 'is_active')
    list_display_links = ('name', 'login')
    search_fields = ('name', 'login', 'door_id')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'time_created')
    prepopulated_fields = {"slug": ("name",)}


class InterfaceAdminDoor(admin.ModelAdmin):
    list_display = ('pk','name', 'url')
    list_display_links = ('name', 'url')
    search_fields = ('name', 'url')
    prepopulated_fields = {"slug": ("name",)}
    
    
class InterfaceAdminHistory(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', 'url')
    search_fields = ('name', 'url')



admin.site.register(User, InterfaceAdminUser)
admin.site.register(Door, InterfaceAdminDoor)





