from django.conf.urls.defaults import patterns, url
from .views import *
from django.contrib.auth.decorators import login_required
from slider.views import *
from fellowship.views import *

urlpatterns = patterns('',
    url(r'^$', login_required(AdminIndex.as_view()), name='dashboard'),
    
    url(r'^events/$', login_required(AdminEvent.as_view()), name='dashboard_event'),
    url(r'^events/new/$', login_required(AdminEventNew.as_view()), name='dashboard_event_new'),
    url(r'^events/edit/(?P<pk>\d+)$', AdminEventUpdate.as_view(), name='dashboard_event_update'),
    url(r'^events/delete/(?P<pk>\d+)$', adminEventDelete, name='dashboard_event_delete'),

    url(r'^fellowship/$', login_required(AdminFellowship.as_view()), name='dashboard_fellowship'),
    
    url(r'^news/$', login_required(AdminNews.as_view()), name='dashboard_news'),
    url(r'^news/new$', login_required(AdminNewsNew.as_view()), name='dashboard_news_new'),
    url(r'^news/edit/(?P<pk>\d+)$', login_required(AdminNewsUpdate.as_view()), name='dashboard_news_update'),
    
    url(r'^service/$', login_required(AdminService.as_view()), name='dashboard_service'),
    url(r'^service/new$', login_required(AdminServiceNew.as_view()), name='dashboard_service_new'),

    url(r'^about/$', login_required(AdminAbout.as_view()), name='dashboard_about'),
    url(r'^about/new$', login_required(AdminAboutNew.as_view()), name='dashboard_about_new'),
    url(r'^about/edit/(?P<pk>\d+)$', login_required(AdminAboutUpdate.as_view()), name='dashboard_about_update'),

    url(r'^member/$', login_required(AdminMembers.as_view()), name='dashboard_staff'),
    url(r'^member/new$', login_required(AdminMembersNew.as_view()), name='dashboard_staff_new'),
    url(r'^member/ministry/new$', login_required(AdminMembersMinistryNew.as_view()), name='dashboard_staff_ministry_new'),

    url(r'^slides/$', login_required(AdminSlideView.as_view()), name='dashboard_slides'),
    url(r'^slides/new/$', login_required(AdminSlideNew.as_view()), name='dashboard_slides_new'),
    url(r'^slides/edit/(?P<pk>\d+)/$', login_required(AdminSlideUpdate.as_view()), name='dashboard_slide_update'),
    url(r'^slides/delete/(\d+)/$', login_required(adminSlideDelete), name='dashboard_slides_delete'),

    url(r'^slides/(\d+)/new_slide_item/$', login_required(AdminNewSlideItem.as_view()), name='dashboard_slides_new_item'),
    url(r'^slides/item/edit/(?P<pk>\d+)/$', login_required(AdminUpdateSlideItem.as_view()), name='dashboard_slides_update_item'),
    url(r'^slides/item/delete/(\d+)/$', login_required(adminSlideItemDelete), name='dashboard_slides_delete_item'),

    url(r'^dashboard_login/$', dashboard_login, name='dashboard_login'),
    url(r'^dashboard_logout/$', dashboard_logout, name='dashboard_logout'),
)
