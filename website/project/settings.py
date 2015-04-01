import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'gunicorn',
    'django_extensions',
    'djangobower',
    'compressor',
    'sekizai',
    'tastypie',
    'ckeditor',
    'lineage',
    'taggit',
    'taggit_templatetags',
    'endless_pagination',
    'adminsortable',
    'fileupload',
    'uploader',
    'blog',
    'projects',
    'pages',
    'gallery'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai'
)

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'


# i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# static configuration
STATICFILES_DIRS = (
    ("img", os.path.join(BASE_DIR, "static/img")),
    ("css", os.path.join(BASE_DIR, "static/css")),
    ("js", os.path.join(BASE_DIR, "static/js")),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
FILES_ROOT = os.path.join(BASE_DIR, 'media/files')
FILES_URL = '/media/files/'

# tastypie
API_VERSION = 'v1'
TASTYPIE_ALLOW_MISSING_SLASH = True

# bower
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'static')
BOWER_INSTALLED_APPS = (
    'backbone',
    'underscore',
    'zurb/bower-foundation',
    'three.js'
)

# wysiwyg settings
CKEDITOR_ROOT = os.path.join(BASE_DIR, 'media/files')
CKEDITOR_URL = '/media/files/'
#CKEDITOR_UPLOAD_PATH = 'files/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'CMS, Full',
        'toolbar_CMS': [
            {
                'name': 'basicstyles',
                'groups': ['basicstyles', 'cleanup'],
                'items': ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat']
            },
            {
                'name': 'paragraph',
                'groups': ['list', 'indent', 'blocks'],
                'items': [
                    'NumberedList', 'BulletedList', '-', 'Outdent',
                    'Indent', '-', 'Blockquote'
                ]
            },
            {
                'name': 'links',
                'items': ['Link', 'Unlink']
            },
            {
                'name': 'insert',
                'items': ['Image', 'HorizontalRule', 'Table', 'Iframe', ]
            },
            {
                'name': 'colors',
                'items': ['TextColor', 'BGColor']
            }
        ],
        'height': 500,
        'width': 1500,
        'skin': 'moono',
        'uiColor': '#aaff00',
        #'startupMode': 'source'
    },
}


# pagination
ENDLESS_PAGINATION_PER_PAGE = 3

# load local_settings
try:
    from local_settings import *
except ImportError:
    pass
