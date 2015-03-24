from django import template
import random

from gallery.models import File

register = template.Library()

@register.assignment_tag
def get_files():
    return File.objects.all()

@register.filter
def shuffle(arg):
    # slice it, cast it to list
    l = list(arg[:])
    random.shuffle(l)
    return l
