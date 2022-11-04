from django.urls import path, include, re_path
from .views import *
from door_manager  import settings
from django.conf.urls.static import static
from captcha.fields import CaptchaField


urlpatterns = [
    path('', DoorHome.as_view(), name = 'home'),
    path('users/', UsersHome.as_view(), name = 'users'),
    path('door/<slug:door_slug>/', UsersDoors.as_view(), name = 'door'),
    path('info/<slug:info_slug>/', ShowUserInfo.as_view(), name = 'info'),
    path('adduser/', AddUser.as_view(), name='adduser'),
    path('about/', about, name='about'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),   
    path('logout/', logout_user, name='logout'),
    path('doors/', doors, name = 'doors'),
    #path('doors/<slug:door>/', edit_door, name = 'edit_door'),
    path('support/', SupportFormView.as_view(), name = 'support'),
    path('history/', history, name = 'history'),
    path('errors/', errors, name = 'errors'),
    path('admin/', errors, name = 'admin'),

    path('<path>/<door_name>', controller_determinant, name='controller_determinant'),

    #re_path(r'^test/(?P<year>[0-9]{4})/', test_error)
    ]


