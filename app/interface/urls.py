from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<path>/<door_name>', views.controller_determinant, name='.controller_determinant'),
]