from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from shop_simplevariations import urls as simplevariations_urls

from apps.myshop import urls as legacy_urls


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^feedback/', include('feedback.urls')),
    url(r'^', include('apps.articles.urls')),
#    (r'^shop/cart/', include(simplevariations_urls)),
    (r'^', include(legacy_urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^media/(?P<path>.*)$', 'serve'),
    )