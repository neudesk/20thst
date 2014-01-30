from django.db import models
from imagekit.processors import ResizeToCover, ResizeToFit
from imagekit.models import ProcessedImageField

class Transition(models.Model):
    transition = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.transition

class Slide(models.Model):

    name = models.CharField(max_length=20)
    transition = models.ForeignKey(Transition)
    slot_amount = models.IntegerField(max_length=2, default=0)
    background_color = models.CharField(max_length=7, blank=True, null=True)
    background = ProcessedImageField(upload_to='slides',
                                     processors=[ResizeToFit(2000, 470)],
                                     format='PNG',
                                     options={'quality': 60}, null=True, blank=True)

    def __unicode__(self):
        return self.name

class DirectionalTransition(models.Model):

    name = models.CharField(max_length=30, unique=True)
    directional_transition = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

class Easing(models.Model):
    easing = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.easing

class StyleClass(models.Model):
    style_class = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.style_class

class SlideItemImage(models.Model):

    name = models.CharField(max_length=30, unique=True)
    image = ProcessedImageField(upload_to='slides',
                                 processors=[ResizeToCover(600, 0)],
                                 format='PNG',
                                 options={'quality': 60})

    def __unicode__(self):
        return self.name

class SlideItem(models.Model):

    slide = models.ForeignKey(Slide)
    slide_text = models.CharField(max_length=30, null=True, blank=True)
    directional_transition = models.ForeignKey(DirectionalTransition)
    animation_easing = models.ForeignKey(Easing)
    animation_speed = models.IntegerField(max_length=5, default=100)
    timing = models.IntegerField(max_length=5, default=300)
    position_x_axis = models.IntegerField(max_length=4, default=0)
    position_y_axis = models.IntegerField(max_length=4, default=0)
    caption_style_class = models.ForeignKey(StyleClass)
    image = ProcessedImageField(upload_to='slides',
                                processors=[ResizeToCover(600, 0)],
                                format='PNG',
                                options={'quality': 60}, null=True, blank=True)

    def __unicode__(self):
        return self.slide_text