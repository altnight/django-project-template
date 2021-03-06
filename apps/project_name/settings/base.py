# -*- coding: utf-8 -*-
"""
Django settings for {{ project_name }} project.
"""

import os
APPS_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),  # settings dir
    os.pardir,  # project dir
    os.pardir,
))
REOPSITORY_DIR = os.path.abspath(os.path.join(
    APPS_DIR,
    os.pardir,
))

SECRET_KEY = '{{ secret_key }}'

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(APPS_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(REOPSITORY_DIR, "statics"),
)

TEMPLATE_DIRS = (
    os.path.join(REOPSITORY_DIR, 'templates'),
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
