import os
import sys


SERVER_ENV = os.environ.get('SERVER_ENV', 'development')

DEBUG = TEMPLATE_DEBUG = (SERVER_ENV == 'development')

SITE_ID = 1
SITE_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

# Import any private settings.
from settings import private
for setting in dir(private):
    if setting == setting.upper():
        setattr(sys.modules[__name__], setting, getattr(private, setting))

MANAGERS = ADMINS

TIME_ZONE = 'Europe/London'
DATE_FORMAT = 'j N y'
TIME_FORMAT = 'g:iA'
DATETIME_FORMAT = ', '.join([TIME_FORMAT, DATE_FORMAT])
MONTH_DAY_FORMAT = 'j F'
LANGUAGE_CODE = 'en-gb'

EMAIL_SUBJECT_PREFIX = '[Refresh Edinburgh] '

ROOT_URLCONF = 'urls'

USE_ETAGS = False

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

TEMPLATE_DEBUG = DEBUG
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'apps.core.context_processors.media_url',
    'apps.core.context_processors.current_site',
)
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates/'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.admin',

    'apps.core',
    'apps.events',
)
