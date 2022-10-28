from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('history/', views.history, name='history'),
    path('<path>/<door_name>', views.controller_determinant, name='.controller_determinant'),
]

