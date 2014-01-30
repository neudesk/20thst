from django import forms
from django.conf import settings
from event.models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib import messages
from django.core.exceptions import ValidationError
import logging

class IncludeCategoryFieldMixin(object):
    category = forms.ModelChoiceField(required=True, queryset=EventCategory.objects.all())
    
class BaseForm(forms.ModelForm):
    details = forms.CharField(widget=CKEditorWidget())
    postType = "event"

    class Meta:
        exclude = ("youtube_video_id",
                   "parent_post",
                   "post_type")
        model = Event

    def clean_cover(self):
        cover = self.cleaned_data.get("cover")
        if hasattr(cover, '_size'):
            if int(cover._size) > settings.ALW_FILE_SIZE:
                raise ValidationError("File size is too large!: Maximum file size allowed is 256kb.")
        return cover
    
    def get_post_type(self):
        try:
            return PostType.objects.get(type=self.postType)
        except Exception as e:
            logging.error(e.message)
            raise forms.ValidationError(e.message)
    
    def save(self, *args, **kwargs):
        instance = super(BaseForm, self).save(commit=False, *args, **kwargs)
        instance.post_type = self.get_post_type()
        instance.save(*args, **kwargs)
            
class EventForm(BaseForm, IncludeCategoryFieldMixin):
    postType = "event"
    
            
class NewsForm(BaseForm):
    postType = "news"
    
    class Meta:
        exclude = ("youtube_url_id",
                   "parent_post",
                   "post_type",
                   "place",
                   "start_date",
                   "end_date",
                   "start_time",
                   "end_time")
        model = Event
    
class WorshipServiceForm(BaseForm):
    postType = "worship_services"
    
    class Meta:
        exclude = ("parent_post",
                   "post_type",
                   "place",
                   "start_date",
                   "end_date",
                   "start_time",
                   "end_time")
        model = Event

class AboutForm(BaseForm):
    postType = "about"

    class Meta:
        exclude = ("parent_post",
                   "post_type",
                   "place",
                   "start_date",
                   "end_date",
                   "start_time",
                   "end_time",
                   "youtube_url_id")
        model = Event
    
    