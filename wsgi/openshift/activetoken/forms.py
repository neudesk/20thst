from datetime import datetime, timedelta
from django import forms
from churchmember.models import Member, MemberTitle
from churchmember.forms import FrontEndRegForm
from .models import Token
from django.contrib.auth.models import User
from django.contrib import messages

class ActivateForm(forms.ModelForm):

    now = datetime.now()
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    facebook = forms.CharField(max_length=50, required=False, label="Facebook Username")
    token = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ActivateForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ["photo",
                                "firstname",
                                "lastname",
                                "facebook",
                                "token"]

    class Meta:
        exclude = ("user",
                   "ministry")
        model = Member

    def get_def_ministry(self):
        ministry = MemberTitle.objects.filter(title="member")[0]
        return ministry

    def get_token(self):
        token_err = "Invalid activation token, Please make a new activation request."
        token_obj = Token.objects.filter(token=self.cleaned_data['token'])[0]
        if token_obj:
            if self.now > token_obj.expiration:
                raise forms.ValidationError(token_err)
            else:
                return token_obj
        else:
            raise forms.ValidationError(token_err)

        return None

    def save(self, *args, **kwargs):
        instance = super(ActivateForm, self).save(commit=False)
        instance.ministry = self.get_def_ministry()
        token = self.get_token()
        if token:
            user = token.user
            user.first_name = self.cleaned_data['firstname']
            user.last_name = self.cleaned_data['lastname']
            user.is_active = True
            user.save()
            instance.user = user
            instance.save()
        return instance

class ResendActivationForm(forms.Form):

    email = forms.EmailField()

    def clean_email(self):
        data = self.cleaned_data['email']
        user = User.objects.filter(email=data)
        did_not_exists = "This email address did not exists."
        if user:
            if user.count() > 1:
                raise forms.ValidationError(did_not_exists)
            return data
        else:
            raise forms.ValidationError(did_not_exists)
        return data

    def create_token(self, email):
        user = User.objects.get(email=email)
        token = Token(user=user)
        token.save()
        return token

    def resend_activation(self, request):
        data = self.cleaned_data
        regForm = FrontEndRegForm()
        token = self.create_token(data['email'])
        try:
            regForm.send_activation_email(data=data, url=reverse_lazy("activate"), token=token.token)
            messages.info(request, "Please check your email to activate your account.")
        except:
            messages.warning(request, "Unable to request activation email at this time, Please try again later.")

