# -*- coding: utf-8 -*-
from {{ project_name }}.settings.base import *  # NOQA

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

####################
# debug toolbar
####################

INSTALLED_APPS += (
    'django.contrib.staticfiles',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

STATIC_URL = '/static/'

####################
# devserver
####################

INSTALLED_APPS += (
    'devserver',
)

MIDDLEWARE_CLASSES += (
    'devserver.middleware.DevServerMiddleware',
)

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # 'devserver.modules.ajax.AjaxDumpModule',
    # 'devserver.modules.profile.MemoryUseModule',
    # 'devserver.modules.cache.CacheSummaryModule',
    # 'devserver.modules.profile.LineProfilerModule',
)
