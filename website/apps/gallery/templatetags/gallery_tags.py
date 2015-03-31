from django import template
import random

from gallery.models import Image

register = template.Library()


@register.inclusion_tag('gallery/templatetags/gallery_inline.html', takes_context=True)
def gallery_inline(context):
    images = Image.objects.all()

    context['images'] = images

    return context


@register.filter
def shuffle(arg):
    # slice it, cast it to list
    l = list(arg[:])
    random.shuffle(l)
    return l
