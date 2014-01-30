from django.db import models

class Donation(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    donated_on = models.DateTimeField(auto_now_add=True)
    ip = models.IPAddressField()
    
    def __unicode__(self):
        return self.amount
    
class Donor(models.Model):
    donation = models.ForeignKey(Donation)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s %s" % (self.firstname,
                           self.lastname)
        
    def set_anonymous(self):
        if self.firstname is None:
            self.firstname = "Anonymous"
        elif self.lastname is None:
            self.lastname = "Anonymous"
            
    def save(self, *args, **kwargs):
        instance = super(Donor, self)
        self.set_anonymous()
        instance.save(*args, **kwargs)
        return instance
    
    