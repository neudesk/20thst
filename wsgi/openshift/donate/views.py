from contact.views import BaseFormView
from django.core.urlresolvers import reverse_lazy
from .forms import DonationForm

class DonationView(BaseFormView):
    title = "Offerings"
    template_name = "donations.djhtml"
    form_class = DonationForm
    success_url = reverse_lazy("donation")
    
    def form_valid(self, form):
        instance = super(DonationView, self)
        form.save(self.request)
        return instance.form_valid(form)