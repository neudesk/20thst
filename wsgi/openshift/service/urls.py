from django.conf.urls.defaults import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', ServiceIndex.as_view(), name='service'),
)
