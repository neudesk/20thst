from django.contrib.sites.models import get_current_site
from django.contrib import messages
from django import forms
from django.conf import settings
from django.http import HttpRequest
from django.core.urlresolvers import reverse_lazy
from activetoken.models import Token
from mailgun.views import MailGun
from django.contrib import auth
from .models import *

class MemberTitleForm(forms.ModelForm):


    LEVEL = (
        ("0", "Church Member / Non-Technical Staff"),
        ("1", "auth 1"),
        ("2", "auth 2"),
        ("3", "auth 3"),
    )
    admin_level = forms.ChoiceField(choices=LEVEL)
    class Meta:
        model = MemberTitle

class MemberForm(forms.ModelForm):

    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    facebook = forms.CharField(max_length=60, required=False, label="Facebook ID")

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ["ministry",
                                 "username",
                                 "password",
                                 "email",
                                 "firstname",
                                 "lastname",
                                 "facebook",
                                 "photo"]

    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if hasattr(photo, '_size'):
            if int(photo._size) > settings.ALW_FILE_SIZE:
                raise forms.ValidationError("File size is too large!: Maximum file size allowed is 256kb.")
        return photo

    class Meta:
        exclude = ("user",)
        model = Member


    def save(self, commit=True):
        data = self.cleaned_data
        instance = super(MemberForm, self).save(commit=False)
        instance.facebook = "%s/%s" % (settings.FB_DEF_URL,
                                       data['facebook'])
        user = User(first_name=data['firstname'],
                    last_name=data['lastname'],
                    email=data['email'],
                    username=data['username'])
        user.set_password(data['password'])

        if int(instance.ministry.admin_level) > 0:
            user.is_staff = True
        user.save()
        instance.user = user
        return instance.save()

class FrontEndRegForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    request = HttpRequest()

    def clean_email(self):
        data = self.cleaned_data['email']
        obj = User.objects.filter(username=data)
        if obj:
            raise forms.ValidationError("Email address is already been registered!")
        return data

    def send_activation_email(self, data=None, url=None, token=None):
        activeurl = "%s%s?token=%s" % (get_current_site(self.request), url, token)
        message = """Please visit the URL or copy and paste the url to your browser to activate your account.
                  <br />
                  Activation URL: <a href="%s" target="_blank">%s</a>
                  <br />
                  This activation token is only valid 24 hours after you register or request it.
                  """ % (activeurl,
                         activeurl)

        mail = MailGun(subject="Account Activation",
                       message=message,
                       fr=settings.MAIL_CHURCH_DEFAULT_MAIL,
                       recipients=[data['email']])
        mail.send()

    def save(self):
        data = self.data
        user = User(username=data['email'],
                    email=data['email'])
        user.set_password(data['password'])
        user.is_active = False
        user.save()
        token = Token(user=user)
        token.save()
        self.send_activation_email(data=data,
                                   url=reverse_lazy("activate"),
                                   token=token.token)

class FrontEndLogIn(forms.Form):

    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    def login(self, request):
        data = self.data
        user = auth.authenticate(username=data['email'],
                                 password=data['password'])
        if user:
            if not user.is_active:
                messages.warning(request,
                                 "inactive account!")
            else:
                auth.login(request, user)
        else:
            messages.warning(request,
                             "Incorrect credentials!")




