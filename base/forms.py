from django.forms import ModelForm
from .models import Photo


class PhotoModelForm(ModelForm):
    class Meta:
        model = Photo
        fields = ["short_title", "image"]
