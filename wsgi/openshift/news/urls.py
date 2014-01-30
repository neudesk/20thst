from django.conf.urls.defaults import patterns, include, url
from .views import NewsIndex, SingleNews

urlpatterns = patterns('',
    url(r'^$', NewsIndex.as_view(), name='news'),
    url(r'^(\d+)/$', SingleNews.as_view(), name='news_by_id'),
)
