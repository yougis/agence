"""
Django settings for agence project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
 
PROJECT_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(*mg%!7ys!h#r$=vk^s14dun#k9hd&u-o)@t2+u6*9l=bb*rq+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',

    'photologue',
    'sortedm2m',
    'catalogue',    
    'django_tables2',
    'widget_tweaks',
    'import_export',    
)

SITE_ID = 1

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
"django.core.context_processors.request",
)

ROOT_URLCONF = 'agence.urls'

WSGI_APPLICATION = 'agence.wsgi.application'
 
MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, '../public/media'))
MEDIA_URL = '/media/'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'hugoroussaffa$qretali_agence',
         'USER': 'hugoroussaffa',
         'PASSWORD': 'agence',
         'HOST': 'mysql.server',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = 'public/static/' 
STATIC_URL = '/static/' if DEBUG else 'http://127.0.0.1:8000/static/' 
