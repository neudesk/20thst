from django.conf.urls.defaults import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', ContactView.as_view(), name='contacts'),
)
