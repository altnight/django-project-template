from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # TODO: add INSTALLED_APPS and use app name
    url(r'^$', include('core.urls', namespace='core', app_name='core')),
    # url(r'^app/', include('app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


# debug toolbar
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',

        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
