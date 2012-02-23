from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

from apps.myshop import urls as legacy_urls


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^feedback/', include('apps.feedback.urls')),
    (r'^callback/', include('apps.callback.urls')),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^', include('apps.articles.urls')),
    (r'^', include(legacy_urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^media/(?P<path>.*)$', 'serve'),
    )