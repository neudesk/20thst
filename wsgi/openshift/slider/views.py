from django_tables2.views import SingleTableView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import Slide
from .tables import *
from .forms import *

def adminSlideItemDelete(request, id):
    instance = get_object_or_404(SlideItem, id=id)
    instance.delete()
    return HttpResponseRedirect(reverse_lazy("dashboard_slides"))

def adminSlideDelete(request, id):
    instance = get_object_or_404(Slide, id=id)
    for i in instance.slideitem_set.all():
        i.delete()
    instance.delete()
    return HttpResponseRedirect(reverse_lazy("dashboard_slides"))

class AdminUpdateSlideItem(UpdateView):

    template_name = "adminslide_newitem.djhtml"
    title = "Slide Builder"
    pagedesc = "This is a rich slide creator for the public website banner display."
    model = SlideItem
    page_name = 'slides'
    form_class = SlideItemForm
    success_url = reverse_lazy("dashboard_slides")

    def get_parent_slide(self, *args, **kwargs):
        item = SlideItem.objects.get(id=self.kwargs['pk'])
        slide = item.slide
        return slide

    def get_table_data(self):
        slide = self.get_parent_slide()
        return SlidesItemsTables(slide.slideitem_set.all())

    def form_valid(self, form):
        self.success_url = self.request.path
        return super(AdminUpdateSlideItem, self).form_valid(form)

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(AdminUpdateSlideItem, self).render_to_response(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(AdminUpdateSlideItem, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['pagedesc'] = self.pagedesc
        context['pagename'] = self.page_name
        context['s'] = self.get_parent_slide()
        context['slide_item_table'] = self.get_table_data()
        return context

class AdminNewSlideItem(CreateView):

    template_name = "adminslide_newitem.djhtml"
    title = "Slide Builder"
    pagedesc = "This is a rich slide creator for the public website banner display."
    model = SlideItem
    page_name = 'slides'
    form_class = SlideItemForm
    success_url = reverse_lazy("dashboard_slides")

    def get_parent_slide(self, *args, **kwargs):
        slide = Slide.objects.get(id=self.args[0])
        return slide

    def get_table_data(self):
        slide = self.get_parent_slide()
        return SlidesItemsTables(slide.slideitem_set.all())

    def form_valid(self, form):
        self.success_url = reverse_lazy("dashboard_slide_update", kwargs={'pk': self.args[0]})
        return super(AdminNewSlideItem, self).form_valid(form)

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(AdminNewSlideItem, self).render_to_response(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(AdminNewSlideItem, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['pagedesc'] = self.pagedesc
        context['pagename'] = self.page_name
        context['s'] = self.get_parent_slide()
        context['slide_item_table'] = self.get_table_data()
        return context

class AdminSlideView(SingleTableView):
    template_name = "adminslide.djhtml"
    title = "Slide Builder"
    pagedesc = "This is a rich slide creator for the public website banner display."
    model = Slide
    page_name = 'slides'
    table_class = SlidesTable

    def get_table_data(self):
        data = self.model.objects.all()
        return data

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(AdminSlideView, self).render_to_response(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(AdminSlideView, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['pagedesc'] = self.pagedesc
        context['pagename'] = self.page_name
        context['slides'] = self.get_table_data()
        return context

class AdminSlideNew(CreateView):
    template_name = "adminslide_new.djhtml"
    title = "Slide Builder"
    pagedesc = "This is a rich slide creator for the public website banner display."
    model = Slide
    page_name = 'slides'
    form_class = SlideForm
    success_url = reverse_lazy("dashboard_slides")

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(AdminSlideNew, self).render_to_response(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(AdminSlideNew, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['pagedesc'] = self.pagedesc
        context['pagename'] = self.page_name
        return context

class AdminSlideUpdate(UpdateView):
    template_name = "adminslide_update.djhtml"
    title = "Slide Builder"
    pagedesc = "This is a rich slide creator for the public website banner display."
    model = Slide
    page_name = 'slides'
    form_class = SlideForm
    success_url = reverse_lazy("dashboard_slides")

    def render_to_response(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse_lazy("frontend_login"))
        else:
            return super(AdminSlideUpdate, self).render_to_response(*args, **kwargs)

    def get_parent_slide(self, *args, **kwargs):
        slide = Slide.objects.get(id=self.kwargs['pk'])
        return slide

    def get_table_data(self):
        slide = self.get_parent_slide()
        return SlidesItemsTables(slide.slideitem_set.all())

    def get_context_data(self, *args, **kwargs):
        context = super(AdminSlideUpdate, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        context['pagedesc'] = self.pagedesc
        context['pagename'] = self.page_name
        context['slide_item_table'] = self.get_table_data
        context['s'] = self.get_parent_slide()
        return context
