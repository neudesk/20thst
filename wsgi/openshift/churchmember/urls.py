from django.conf.urls.defaults import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', RegFormIndex.as_view(), name='register'),
    url(r'^frontend_login/$', LoginIndex.as_view(), name='frontend_login'),
    url(r'^frontend_logout/$', frontend_logout, name='frontend_logout'),
)
