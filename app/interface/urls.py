from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('history/', views.history, name='history'),
    path('adduser/', views.adduser, name='adduser'),
    path('logs/', views.logs, name='logs'),
    path('<path>/<door_name>', views.controller_determinant, name='controller_determinant'),

]

