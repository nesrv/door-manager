from django import template

# from door_manager.door.models import Door

from door.models import *

register = template.Library()


@register.simple_tag(name='getdoors')
def get_door(filter=None):
    if not filter:
        return Door.objects.all()
    else:
        return Door.objects.filter(pk=filter)


@register.inclusion_tag('door/list_door.html')
def show_doors(sort=None, door_selected=0):
    if not sort:
        doors = Door.objects.all()
    else:
        doors = Door.objects.order_by(sort)

    return {"doors": doors, "door_selected": door_selected}


@register.simple_tag(name='getusers')
def get_user(filter=None):
    if not filter:
        return User.objects.all()
    else:
        return User.objects.filter(pk=filter)
