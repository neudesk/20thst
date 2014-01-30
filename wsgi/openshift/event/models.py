from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToCover
# from comment.models import Comment

class PostType(models.Model):
    type = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.type

class EventCategory(models.Model):
    category = models.CharField(max_length=60, unique=True)
#     post_type = models.ForeignKey(PostType, related_name="category_post_type")
    
    def __unicode__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = "Categories"

class Event(models.Model):
    
    post_type = models.ForeignKey(PostType, related_name="event_post_type")
    # category = models.ForeignKey(EventCategory, blank=True, null=True)
    title = models.CharField(max_length=90)
    details = RichTextField()
    youtube_video_id = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=250, blank=True, null=True)
    cover = models.ImageField(upload_to='uploads')
    cover_thumbnail = ImageSpecField(source='cover',
                                     processors=[ResizeToCover(286, 0)],
                                     format='PNG',
                                     options={'quality': 60})
    cover_banner = ImageSpecField(source='cover',
                                  processors=[ResizeToCover(800, 0)],
                                  format='PNG',
                                  options={'quality': 60})
    is_pub = models.BooleanField(default=True)
#     comment = models.ManyToManyField(Comment, blank=True, null=True)
    parent_post = models.ForeignKey('self', null=True, blank=True)
    posted_by = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    