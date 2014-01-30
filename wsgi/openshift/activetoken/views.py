from churchmember.views import *
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import *

class ActivateIndex(RegFormIndex):
    template_name = "activeindex.djhtml"
    form_class = ActivateForm
    title = "Activate"
    success_url = reverse_lazy("frontend_login")

    def form_valid(self, form):
        try:
            form.save()
        except Exception as e:
            messages.warning(self.request, e)
        return super(ActivateIndex, self).form_valid(form)

    def render_to_response(self, context):
        try:
            token = self.request.GET['token']
        except:
            messages.warning(self.request, "Invalid activation token: <a href='%s' class='pull-right'>Resend Activation Email?</a>" % reverse_lazy("resend_activation"))
            return HttpResponseRedirect(reverse_lazy("register"))
        return super(ActivateIndex, self).render_to_response(context)

class ResendActivation(RegFormIndex):
    template_name = "requestactivation.djhtml"
    form_class = ResendActivationForm
    title = "Resend Activation"
    success_url = reverse_lazy("resend_activation")

    def form_valid(self, form):
        form.ResendActivation(self.request)
        return super(ResendActivation, self).form_valid(form)