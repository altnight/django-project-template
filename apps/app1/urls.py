# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from {{ app_name }}.views import some_view

urlpatterns = patterns(
    '{{ app_name }}.views',

    url(
        regex=r'^(?P<slug>\w+)/?$',
        view=some_view,
        name='simple_view',
    ),
)
