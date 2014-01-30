from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from .views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeIndex.as_view(), name='home'),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^dashboard/', include('dashboard.urls')),
    (r'^event/', include('event.urls')),
    (r'^service/', include('service.urls')),
    (r'^ebible/', include('ebible.urls')),
    (r'^news/', include('news.urls')),
    (r'^contacts/', include('contact.urls')),
    (r'^offerings/', include('donate.urls')),
    (r'^authentication/', include('churchmember.urls')),
    (r'^activate/', include('activetoken.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.STATIC_ROOT,
    }),
)
