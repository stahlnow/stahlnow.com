import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

ALLOWED_HOSTS = ['*',]
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
    # 'tastypie',
    'lineage',
    'taggit',
    'taggit_templatetags2',
    'el_pagination',
    'easy_thumbnails',
    'adminsortable2',
    'fileupload',
    # 'uploader',
    'filer',
    'mptt',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                # sekizai
                'sekizai.context_processors.sekizai',
            ],
            'loaders': [
                # admin tools
                # 'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'


# i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Zurich'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# static configuration
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'site-static'),
)
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
FILES_ROOT = os.path.join(BASE_DIR, 'media/files')
FILES_URL = '/media/files/'


THUMBNAIL_BASEDIR = 'files'

# filer
FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': os.path.join(BASE_DIR, 'media/files'),
                'base_url': '/media/files/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': os.path.join(BASE_DIR, 'media/files'),
                'base_url': '/media/files/',
            },
        },
    },
}

# tastypie
# API_VERSION = 'v1'
# TASTYPIE_ALLOW_MISSING_SLASH = True

# bower
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'site-static')
BOWER_INSTALLED_APPS = (
    'backbone#1.2.1',
    'csshake',
    'underscore#1.8.3',
    'jquery-placeholder#2.0.8',
    'foundation#5.5.2',
    'modernizr#2.8.3',
    'fastclick#1.0.3',
    'jquery#2.1.3',
    'jquery.cookie#1.4.1',
    'three.js#0.71.0'
)


# pagination
ENDLESS_PAGINATION_PER_PAGE = 3

# taggit tag cloud
TAGGIT_LIMIT = 10000

# load local_settings
try:
    from local_settings import *
except ImportError:
    pass
