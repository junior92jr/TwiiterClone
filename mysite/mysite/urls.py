from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
	url(r'^twitterclone/', include('twitterclone.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )