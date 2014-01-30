from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, resolve_url
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Event, EventCategory, PostType
from comment.models import Comment
from openshift.views import HomeIndex
from datetime import datetime as dt

class EventIndex(HomeIndex):
    template_name = "eventindex.djhtml"
    title = "events"
    submodels = {'comments': Comment}
    model = Event
    postType = PostType.objects.filter(type="event")
    
    def get_query(self):
        obj = {}
        for k, v in self.submodels.items():
            obj[k] = v.objects.order_by('-id')
        return obj
    
    def get_post(self):
        now = dt.now()
        if self.postType:
            try:
                return self.model.objects.filter(is_pub=True,
                                                 category=self.args[0],
                                                 post_type=self.postType[0],
                                                 start_date__gte=now).order_by('-start_date')
            except:
                return self.model.objects.filter(is_pub=True,
                                                 post_type=self.postType[0],
                                                 start_date__gte=now).order_by('-start_date')
        else:
            return None
    
    def get_context_data(self, *args, **kwargs):
        context = super(EventIndex, self).get_context_data(*args, **kwargs)
        context.update(self.get_query())
        context['post'] = self.get_post()
        return context

class SingleEvent(EventIndex):
    template_name = "eventsingle.djhtml"

    def get_post(self):
        post = get_object_or_404(Event, id=self.args[0])
        return post
    
    def get_context_data(self, *args, **kwargs):
        context = super(SingleEvent, self).get_context_data(*args, **kwargs)
        post = self.get_post()
        context['title'] = post.title
        return context
    
def createEventComment(request):
    event_id = request.POST['event_id']
    e = get_object_or_404(Event, id=event_id)
    if request.POST['message'] != "":
        c = Comment(user=request.user,
                    message=request.POST['message'],
                    event=e)
        try:
            c.save()
        except Exception as err:
            messages.error(request, "Error: %s" % err)
    else:
        messages.error(request, "Error: Please don't submit the field blank!")
    
    return HttpResponseRedirect(resolve_url(request.POST['next']))
