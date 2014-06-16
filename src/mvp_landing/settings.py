"""
Django settings for mvp_landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

#aba added can be used with gmail
from .email_info import *
EMAIL_US_TLS = EMAIL_US_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD= EMAIL_HOST_PASSWORD
EMAIL_PORT =EMAIL_PORT
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#aba added BASE_URL=C:\djangoTestScripts\skillshare\src

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kk8n9(z4luoas#_sd0n830czd%w79&v3@1x+z+m8)klf^!04w3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG #ABA changed this from DEBUG instead of true

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'signups'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mvp_landing.urls'

WSGI_APPLICATION = 'mvp_landing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#template location
TEMPLATE_DIRS=(
    #goes to right outside the app and joins that folder to static. the base dir is defined higher up. and it is defined to the folder one up from the base dir which is the folder that contains the settings.py. that folder is src. os.path.dirname goes tothe directory, whne used 3 tiems it goes to skillshare. it equates to skillshare/static/templates
    os.path.join(os.path.dirname(BASE_DIR),"static","templates"),
    #C:\djangoTestScripts\skillshare\static/templates
)

if DEBUG:
    MEDIA_URL='/media/'
    STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR), "static","static-only") #files are collected here
    MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR), "static","media") #media collected here
    STATICFILES_DIRS=(
        os.path.join(os.path.dirname(BASE_DIR),"static","static"),#where u put your static files and when u server them they go to static_root
    )