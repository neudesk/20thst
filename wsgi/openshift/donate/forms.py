from django import forms
from donate.models import Donation, Donor
from billing import get_gateway, CreditCard
from django.contrib import messages

class DonationForm(forms.ModelForm):
    cc_number = forms.CharField(max_length=24, label="Credit Card Number")
    cc_verification = forms.CharField(max_length=3, label="Verification(CCV)")
    cc_month = forms.CharField(max_length=2, label="Expiration Month")
    cc_year = forms.CharField(max_length=4, label="Expiration Year")
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField()
    
    gw = get_gateway("pay_pal")
    
    class Meta:
        exclude = ("ip",)
        model = Donation
        
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def set_cent(self):
        data = self.cleaned_data
        cents = float(data['amount']) * 100
        return cents
    
    def purchase(self, request):
        data = self.cleaned_data
        gw = self.gw.purchase(data['amount'], self.create_cc(request), options={'request': request})
        return gw
    
    def create_cc(self, request):
        data = self.cleaned_data
        cc = CreditCard(first_name=data['firstname'],
                        last_name=data['lastname'],
                        month=data['cc_month'],
                        year=data['cc_year'],
                        number=data['cc_number'],
                        verification_value=data['cc_verification'])
        return cc
    
    def save(self, request, commit=True):
        instance = super(DonationForm, self).save(commit=False)
        instance.ip = self.get_client_ip(request)
        data = self.cleaned_data
        
        if self.create_cc(request).is_valid():
            purchase = None
            try:
                purchase = self.purchase(request)
            except Exception as e:
                messages.warning(request,
                                 "Unable to process your request at this time, Please try again later.")
            if purchase:
                if purchase.get("status") == "SUCCESS" or purchase.get("status") == "SUCCESSWITHWARNING":
                    messages.info(request,
                                  "You have successfully made your donation, Please check your email for confirmation.")
                    instance.save()
                    donor = Donor(donation=instance,
                                  firstname=data['firstname'],
                                  lastname=data['lastname'],
                                  email=data['email'])
                    donor.save()
                else:
                    response = purchase.get("response")
                    messages.warning(request,"%s: %s" % (purchase.get("status"), response.message))   
        else:
            messages.warning(request, "You have entered an invalid card number or verification.")

        return instance
        
        