from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToCover

class Album(models.Model):
    title = models.CharField(max_length=30)
    caption = models.CharField(max_length=150)
    posted = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galleries"

class Photo(models.Model):
    album = models.ForeignKey(Album)
    caption = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='uploads/gallery')
    photo_thumbnail = ImageSpecField(source='cover',
                                     processors=[ResizeToCover(286, 0)],
                                     format='PNG',
                                     options={'quality': 60})

    def __unicode__(self):
        return u"%s" % self.album.title