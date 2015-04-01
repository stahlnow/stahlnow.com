import mimetypes
import os.path
import random
import string

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify

file_store = FileSystemStorage(
    location=settings.CKEDITOR_ROOT, base_url=settings.CKEDITOR_URL)


class NotAnImageException(Exception):
    pass


def slugify_filename(filename):
    """ Slugify filename """
    name, ext = os.path.splitext(filename)
    slugified = get_slugified_name(name)
    return slugified + ext


def get_slugified_name(filename):
    slugified = slugify(filename)
    return slugified or get_random_string()


def get_random_string():
    return ''.join(random.sample(string.ascii_lowercase * 6, 6))


def get_thumb_filename(file_name):
    """
    Generate thumb filename by adding _thumb to end of
    filename before . (if present)
    """
    return unicode('{0}_thumb{1}').format(*os.path.splitext(file_name))


def get_image_format(extension):
    mimetypes.init()
    return mimetypes.types_map[extension.lower()]


def get_media_url(path):
    """
    Determine system file's media URL.
    """
    return file_store.url(path)
