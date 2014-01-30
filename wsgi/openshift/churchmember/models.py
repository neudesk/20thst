from django.db import models
from django.contrib.auth.models import User
from imagekit.processors import ResizeToCover
from imagekit.models import ImageSpecField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class MemberTitle(models.Model):
    title = models.CharField(max_length=30)
    admin_level = models.IntegerField(max_length=1, default=0)

    def __unicode__(self):
        return self.title

class Member(models.Model):
    user = models.ForeignKey(User)
    ministry = models.ForeignKey(MemberTitle)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='uploads/members')
    avatar = ImageSpecField(source='photo',
                            processors=[ResizeToCover(100, 0)],
                            format='PNG',
                            options={'quality': 60})

    def __unicode__(self):
        return u"%s" % (self.user.username)

# @receiver(pre_delete, sender=Member)
# def member_pre_delete(sender, **kwargs):
#     instance = kwargs['instance']
#     user = instance.user
#     user.delete()