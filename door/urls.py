from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    path('', DoorHome.as_view(), name='home'),
    path('users/', UsersHome.as_view(), name='users'),
    path('door/<slug:door_slug>/', UsersDoors.as_view(), name='door'),
    path('info/<slug:info_slug>/', ShowUserInfo.as_view(), name='info'),
    path('adduser/', AddUser.as_view(), name='adduser'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('support/', SupportFormView.as_view(), name='support'),
    path('history/', history, name='history'),
    path('error/', ErrorPage.as_view(), name='error'),
    path('<path>/<door_name>', controller_determinant, name='controller_determinant'),

    # re_path(r'^test/(?P<year>[0-9]{4})/', test_error)
]
