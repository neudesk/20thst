from openshift.views import HomeIndex
from django.views.generic import FormView
from openshift.views import EventCounterMixin
from .forms import ContactForm
from django.core.urlresolvers import reverse_lazy

class BaseFormView(FormView, EventCounterMixin):
    
    def get_context_data(self, *args, **kwargs):
        context = super(BaseFormView, self).get_context_data(*args, **kwargs)
        if self.get_event_counter():
            context['eventcounter'], context['featevent'] = self.get_event_counter()
        context['title'] = self.title
        return context

class ContactView(BaseFormView):
    title = "Contacts"
    template_name = "contacts.djhtml"
    form_class = ContactForm
    success_url = reverse_lazy("contacts")
    
    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(*args, **kwargs)
        if self.get_event_counter():
            context['eventcounter'], context['featevent'] = self.get_event_counter()
        context['title'] = self.title
        return context
    
    def form_valid(self, form):
        instance = super(ContactView, self)
        form.send_mail(self.request)
        return instance.form_valid(form)
    