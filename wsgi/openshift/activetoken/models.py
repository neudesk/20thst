from django.db import models
from django.contrib.auth.models import User
from uuidfield import UUIDField
from datetime import datetime, timedelta

class Token(models.Model):
    user = models.ForeignKey(User)
    token = UUIDField(auto=True)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField(null=True, blank=True)
    now = datetime.now()

    def __unicode__(self):
        return u"%s" % (self.token)

    def save(self, *args, **kwargs):
        instance = super(Token, self)
        exp = self.now + timedelta(days=1)
        self.expiration = exp
        return instance.save()