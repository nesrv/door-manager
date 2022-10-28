from django.contrib import admin

from .models import *


class InterfaceAdminUser(admin.ModelAdmin):
    list_display = ('name', 'login', 'door_id')
    list_display_links = ('name', 'login')
    search_fields = ('name', 'login', 'door_id')

class InterfaceAdminDoor(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', 'url')
    search_fields = ('name', 'url')
class InterfaceAdminHistory(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name', 'url')
    search_fields = ('name', 'url')



admin.site.register(User, InterfaceAdminUser)
admin.site.register(Door, InterfaceAdminDoor)
