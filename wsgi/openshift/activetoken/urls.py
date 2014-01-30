from django.conf.urls.defaults import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', ActivateIndex.as_view(), name='activate'),
    url(r'^resend_activation/$', ResendActivation.as_view(), name='resend_activation'),
)
