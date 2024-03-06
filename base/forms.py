from django import forms
from .models import Photo


class PhotoModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["short_title", "image"]

    def clean_image(self):
        """Checks if image size is less than
        a 100kilobyte
        """
        image = self.cleaned_data["image"]
        image_size_kb = image.size / 2**10
        if image_size_kb > 100:
            raise forms.ValidationError(
                "Image size should not be more thank 100 kilobytes."
            )
        return image
