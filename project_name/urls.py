from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # TODO: add INSTALLED_APPS and use app name
    # url(r'^$', '{{ project_name }}.views.core', name=''),
    # url(r'^app/', include('app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
