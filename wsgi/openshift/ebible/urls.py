from django.conf.urls.defaults import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^apiviewer/$', apiviewer, name='apiviewer'),
    url(r'^$', Books.as_view(), name='ebible'),
    url(ur'^(.*)/$', Books.as_view(), name='ebible_chapter'),
)
