from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, UpdateView


from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from event.models import *
from openshift.views import AdminBaseView
from openshift.tables import *
from .forms import *
from churchmember.models import *
from churchmember.forms import *
from slider.models import *

class BaseView(TemplateView):
    template_name = None
    postType = None
    title = None
    pagedesc = None
    model = None
    page_name = None
    
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
                object = self.model.objects.filter(post_type=self.get_post_type()).order_by('-id')
                return object
            except:
                pass
                
        return None
    
    def get_context_data(self, *args, **kwargs):
        context = super(BaseView, self).get_context_data(*args, **kwargs)
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
            return super(BaseView, self).render_to_response(*args, **kwargs)
    
class BaseCreate(CreateView):
    
    template_name = None
    title = None
    pagedesc = None
    form_class = None
    page_name = None
    success_url = None

    # def form_valid(self, form):
    #     if not form.cover:
    #         form.cover.delete()
    #     return super(BaseCreate, self).form_valid(form)
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(BaseCreate, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['pagedesc'] = self.pagedesc
        context['pagename'] = self.page_name
        return context
    
    def get_success_url(self):
        """
        Returns the supplied URL.
        """
        if self.success_url:
            url = self.success_url #% self.object.__dict__
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model.")
        return url

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(BaseCreate, self).render_to_response(*args, **kwargs)

class BaseUpdate(UpdateView):
    
    template_name = None
    title = None
    pagedesc = None
    form_class = None
    page_name = None
    success_url = None
    
    def get_context_data(self, *args, **kwargs):
        context = super(BaseUpdate, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['pagedesc'] = self.pagedesc
        context['pagename'] = self.page_name
        return context
    
    def get_success_url(self):
        """
        Returns the supplied URL.
        """
        if self.success_url:
            url = self.success_url #% self.object.__dict__
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model.")
        return url

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(BaseUpdate, self).render_to_response(*args, **kwargs)
    
class BaseDelete(DeleteView):
    model = None
    success_url = None
    
    def get_success_url(self):
        """
        Returns the supplied URL.
        """
        if self.success_url:
            url = self.success_url #% self.object.__dict__
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model.")
        return url

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(BaseDelete, self).render_to_response(*args, **kwargs)

class AdminIndex(BaseView):
    template_name = 'dashboard.djhtml'
    page_name = "dashboard"

class AdminEvent(AdminBaseView):
    template_name = 'event.djhtml'
    postType = "event"
    model = Event
    title = "Events"
    pagedesc = "List of all church's events."
    page_name = "event"
    table_class = AdminBaseTable
    
class AdminEventNew(BaseCreate):
    
    template_name = "eventnew.djhtml"
    title = "New Event"
    pagedesc = "This page will let you add a new church events."
    form_class = EventForm
    page_name = "event"
    success_url = reverse_lazy("dashboard_event")

class AdminEventUpdate(BaseUpdate):

    template_name = "eventnew.djhtml"
    title = "Updating Event"
    pagedesc = "This page will let you add a new church events."
    form_class = EventForm
    page_name = "event"
    success_url = reverse_lazy("dashboard_event")
    model = Event
    
class AdminNews(AdminEvent):
    template_name = 'news.djhtml'
    postType = "news"
    title = "News"
    pagedesc = "List of all church's news."
    page_name = "news"
    
class AdminNewsNew(AdminEventNew):
    template_name = "newsnew.djhtml"
    title = "New News"
    pagedesc = "This page will let you add a new church news."
    form_class = NewsForm
    page_name = "news"
    success_url = reverse_lazy("dashboard_news")
    
class AdminNewsUpdate(AdminEventUpdate):
    template_name = "eventnew.djhtml"
    title = "Updating News"
    pagedesc = "This page will let you update church news."
    form_class = NewsForm
    page_name = "news"
    success_url = reverse_lazy("dashboard_news")
    
class AdminService(AdminEvent):
    template_name = 'service.djhtml'
    postType = "worship_service"
    title = "Worship Service"
    pagedesc = "Weekly Worship Service Ceremony"
    page_name = "service"
    
class AdminServiceNew(AdminNewsNew):
    template_name = "servicenew.djhtml"
    title = "New Service"
    pagedesc = "This page will let you add a new church worship service."
    form_class = WorshipServiceForm
    page_name = "service"
    success_url = reverse_lazy("dashboard_service")

class AdminAbout(AdminService):
    template_name = 'about.djhtml'
    postType = "about"
    title = "About The Church"
    pagedesc = "This page will let you add informations about the church i.e. Mission and Vision"
    page_name = "about"

class AdminAboutNew(AdminServiceNew):
    template_name = "aboutnew.djhtml"
    title = "About The Church"
    pagedesc = "This page will let you add a new article about the Church."
    form_class = AboutForm
    page_name = "about"
    success_url = reverse_lazy("dashboard_about")

class AdminAboutUpdate(AdminNewsUpdate):
    template_name = "aboutnew.djhtml"
    title = "About The Church"
    pagedesc = "This page will let you update church about infos."
    form_class = AboutForm
    page_name = "about"
    success_url = reverse_lazy("dashboard_about")

def adminEventDelete(request, pk):
    event = Event.objects.get(id=pk)
    next = request.GET['next']
    try:
        if event.delete():
            for c in event.comment_set.all():
                c.delete()
    except Exception as e:
        messages.error(request, e)
    return HttpResponseRedirect(next)

class AdminMembers(TemplateView):

    template_name = "member.djhtml"
    title = "Staffs, Admin and Members"
    pagedesc = "This is a list of all Church of Christ online members, staff and admins."
    model = Member
    page_name = "member"

    def get_member(self):
        member = self.model.objects.all()
        return member

    def get_context_data(self, *args, **kwargs):
        context = super(AdminMembers, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['pagedesc'] = self.pagedesc
        context['pagename'] = self.page_name
        context['post'] = self.get_member()
        return context

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(AdminMembers, self).render_to_response(*args, **kwargs)

class AdminMembersNew(AdminAboutNew):
    template_name = "membernew.djhtml"
    title = "Add Church Officers"
    pagedesc = "This page will let you add a new Church admin or staff."
    form_class = MemberForm
    page_name = "member"
    success_url = reverse_lazy("dashboard")

class AdminMembersMinistryNew(AdminMembersNew):
    template_name = "ministrynew.djhtml"
    title = "Add new Church Officers Ministry"
    pagedesc = "This page will let you add a new Admin or Staff Ministry"
    form_class = MemberTitleForm
    page_name = "member"
    success_url = reverse_lazy("dashboard_staff")

    def form_valid(self, form):
        if self.request.GET['next']:
            self.success_url = self.request.GET['next']
        return super(AdminMembersMinistryNew, self).form_valid(form)

class AdminSlide(AdminMembers):
    template_name = "slides.djhtml"
    title = "Slides Builder"
    pagedesc = "This a frontend slides builder tool."
    model = Member
    page_name = "slides"

    def get_slides(self):
        slide = Slide.objects.all()
        return slide

    def get_context_data(self, *args, **kwargs):
        context = super(AdminSlide, self).get_context_data(*args, **kwargs)
        context['slides'] = self.get_slides()
        return context

def dashboard_login(request):
    template = "dashboard_login.djhtml"
    if request.user.is_authenticated() and request.user.is_staff:
        return HttpResponseRedirect(reverse_lazy("dashboard"))

    if request.POST:
        data = request.POST
        username = data['username']
        password = data['password']
        next = data['next']
        user = auth.authenticate(username=username,
                                 password=password)
        if user:
            if not user.is_staff:
                messages.error(request, 'Non-Administrator are not allowed to log in this page.')
            elif not user.is_active:
                messages.error(request, "You're account is deactivated, Please contact us!")
            if user and user.is_active and user.is_staff:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy("dashboard"))
        else:
            messages.error(request, 'Incorrect login credentials.')
    return render_to_response(template, 
                              context_instance=RequestContext(request))
def dashboard_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy("dashboard_login"))