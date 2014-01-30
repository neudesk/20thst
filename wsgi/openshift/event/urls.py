from django.conf.urls.defaults import patterns, include, url
from .views import EventIndex, SingleEvent, createEventComment

urlpatterns = patterns('',
    url(r'^$', EventIndex.as_view(), name='event'),
    # url(r'^category/(\d+)/$', EventIndex.as_view(), name='event_by_category'),
    url(r'^(\d+)/$', SingleEvent.as_view(), name='event_by_id'),
    url(r'^comment/$', createEventComment, name='create_event_comment'),
)
