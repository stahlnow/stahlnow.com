from django import template
import random

from gallery.models import Gallery

register = template.Library()

@register.inclusion_tag('gallery/templatetags/gallery_inline.html', takes_context=True)
def gallery_inline(context, name):
    try:
        images = Gallery.objects.get(name=name).images.order_by('?')
        context['images'] = images
    except:
        pass
    return context
