from django import template
import random

from gallery.models import File

register = template.Library()


@register.inclusion_tag('gallery/templatetags/gallery_inline.html', takes_context=True)
def gallery_inline(context):
    files = File.objects.all()

    context['files'] = files

    return context


@register.filter
def shuffle(arg):
    # slice it, cast it to list
    l = list(arg[:])
    random.shuffle(l)
    return l
