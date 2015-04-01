import os

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if 'ckeditor' in settings.INSTALLED_APPS:
    # Confirm CKEDITOR_UPLOAD_PATH setting has been specified.
    try:
        settings.CKEDITOR_ROOT
    except AttributeError:
        raise ImproperlyConfigured("django-ckeditor requires \
                CKEDITOR_ROOT and CKEDITOR_URL setting.")
