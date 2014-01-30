from django.db import models
from django.contrib.auth.models import User
from event.models import Event

class Comment(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    message = models.CharField(max_length=350)
    is_pub = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u"%s" % self.user.username