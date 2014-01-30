from .models import *
from django import forms
from django.conf import settings

class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide

    def clean_background(self):
        background = self.cleaned_data.get("background")
        if hasattr(background, '_size'):
            if int(background._size) > settings.ALW_FILE_SIZE:
                raise forms.ValidationError("File size is too large!: Maximum file size allowed is 256kb.")
        return background

class SlideItemForm(forms.ModelForm):
    class Meta:
        model = SlideItem

    def clean_slide_image(self):
        image = self.cleaned_data.get("image")
        if hasattr(image, '_size'):
            if int(image._size) > settings.ALW_FILE_SIZE:
                raise forms.ValidationError("File size is too large!: Maximum file size allowed is 256kb.")
        return image
