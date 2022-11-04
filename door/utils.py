from django.db.models import Count

from .models import *

menu = [
    {'title': "Manager", 'url_name': 'home'},
    {'title': "Users", 'url_name': 'users'},
    {'title': "Add user", 'url_name': 'adduser'},
    {'title': "History", 'url_name': 'history'},
    {'title': "Error log", 'url_name': 'errors'},
    {'title': "About", 'url_name': 'about'},
    {'title': "Support", 'url_name': 'support'},
    
]


class DataMixin:
    paginate_by = 2
    
    
    def get_user_context(self, **kwargs):
        context = kwargs        
        doors = Door.objects.all()        
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            for _ in range(3):
                user_menu.pop(2)           
        
        context['menu'] = user_menu
        context['door'] = doors
        if 'door_selected' not in context:
            context['door_selected'] = 0
        return context
