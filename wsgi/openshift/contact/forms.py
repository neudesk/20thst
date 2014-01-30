from django import forms
import requests
from django.conf import settings
from event.models import Event
from django.contrib import messages
from mailgun.views import MailGun

class ContactForm(forms.Form):
    
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length=450, required=True, widget=forms.Textarea())
        
    def send_mail(self, request):
        data = self.cleaned_data
        try:
            mail = MailGun(subject="Website Inquiry",
                           message=data['message'],
                           fr=data['email'],
                           recipients=[settings.MAIL_CHURCH_DEFAULT_MAIL])
            mail.send()
            messages.info(request,
                          "You have successfuly sent a message, We will get back to you ASAP.")
        except Exception as e:
            messages.warning(request,
                           "We are not able to deliver you message at this time for the following reasons: %s <br /> Please try again later." % e)
            