from django_tables2 import SingleTableView
from .tables import AdminEventTable, AdminBaseTable
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from datetime import datetime as dt
from event.models import *
from contact.forms import *
from churchmember.forms import FrontEndLogIn
from slider.models import Slide

class EventCounterMixin(object):
    def get_event_query(self):
        postType = PostType.objects.filter(type="event")
        now = dt.now()
        try:
            event = Event.objects.filter(is_pub=True,
                                         post_type=postType[0]).order_by('start_date')
            if event:
                return event
        except:
            return None
    
    def get_event_counter(self):
        if self.get_event_query():
            event = self.get_event_query()[0]
            now = dt.now()
            date = event.start_date
            time = event.start_time
            start = dt(date.year,
                       date.month,
                       date.day,
                       time.hour,
                       time.minute
                       )
            if start > now:
                dif = start - now
                return dif.total_seconds(), event        
        return None
    

class HomeIndex(TemplateView, EventCounterMixin):
    template_name = 'frontend/home/home.djhtml'
    title = "where the bible speaks, we speaks. where the bible is silent, we are silent."
    now = dt.now()
    
    def get_post_type(self, type):
        try:
            return PostType.objects.get(type=type)
        except Exception as e:
            messages.warning(self.request,
                             "Post type %s can't be found!: Please contact web developer!" % type)
            return None
    
    def get_current_events(self):
        post_type = self.get_post_type("event")
        return Event.objects.filter(start_date__gte=self.now,
                                    is_pub=True,
                                    post_type=post_type).order_by("-start_date")[0:3]
    
    def get_previous_events(self):
        post_type = self.get_post_type("event")
        return Event.objects.all().filter(is_pub=True,
                                          post_type=post_type).order_by("-start_date")[0:3]

    def get_church_about(self):
        post_type = self.get_post_type("about")
        return Event.objects.all().filter(is_pub=True,
                                          post_type=post_type).order_by("-id")[0:3]

    def get_church_news(self):
        post_type = self.get_post_type("news")
        return Event.objects.all().filter(is_pub=True,
                                          post_type=post_type).order_by("-id")[0:3]

    def get_slides(self):
        slide = Slide.objects.all()
        return slide


    def get_context_data(self, *args, **kwargs):
        context = super(HomeIndex, self).get_context_data(*args, **kwargs)
        if self.get_event_counter():
            context['eventcounter'], context['featevent'] = self.get_event_counter()
        context['title'] = self.title
        context['current_events'] = self.get_current_events()
        context['previous_events'] = self.get_previous_events()
        context['about'] = self.get_church_about()
        context['latest_news'] = self.get_church_news()
        context['form'] = FrontEndLogIn()
        context['slides'] = self.get_slides()
        return context

class AdminBaseView(SingleTableView):
    template_name = None
    postType = None
    title = None
    pagedesc = None
    model = None
    page_name = None
    table_class = None

    def get_post_type(self):
        if self.postType:
            try:
                data = PostType.objects.filter(type=self.postType)
                if data:
                    return data[0]
            except:
                pass

        return None

    def get_post(self):
        if self.get_post_type():
            try:
                obj = self.model.objects.filter(post_type=self.get_post_type()).order_by('-id')
                return obj
            except:
                pass

        return {}

    def get_table_data(self, *args, **kwargs):
        data = self.get_post()
        return data


    def get_context_data(self, *args, **kwargs):
        context = super(AdminBaseView, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['pagedesc'] = self.pagedesc
        context['pagename'] = self.page_name
        if self.get_post():
            context['post'] = self.get_post()
        return context

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(AdminBaseView, self).render_to_response(*args, **kwargs)