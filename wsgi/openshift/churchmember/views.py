from .forms import *
from django.http import HttpResponseRedirect
from openshift.views import EventCounterMixin, HomeIndex
from contact.views import BaseFormView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

class IsAuthMixin(BaseFormView):
    def render_to_response(self, *args, **kwargs):
        instance = super(IsAuthMixin, self)
        if self.request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy("home"))
        return instance.render_to_response(*args, **kwargs)

class LoginIndex(IsAuthMixin):
    template_name = "frontend_login.djhtml"
    title = "Log In"
    form_class = FrontEndLogIn
    success_url = reverse_lazy("frontend_login")

    def form_valid(self, form):
        instance = super(LoginIndex, self)
        form.login(self.request)
        return instance.form_valid(form)


class RegFormIndex(IsAuthMixin):
    template_name = "regindex.djhtml"
    form_class = FrontEndRegForm
    title = "Register"
    success_url = reverse_lazy("frontend_login")

    def form_valid(self, form):
        try:
            form.save()
            messages.info(self.request, "Congratulations, Please check your email to activate your account.")
        except Exception as e:
            messages.warning(self.request, e)
            self.success_url = reverse_lazy("register")
        return super(RegFormIndex, self).form_valid(form)

def frontend_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy("home"))



