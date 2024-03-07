from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email:
            return email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use by another user.")
        return email


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email:
            return email
        email_exists = (
            User.objects.exclude(id=self.instance.id).filter(email=email).exists()
        )
        if email_exists:
            raise forms.ValidationError("Email already in use by another user.")
        return email


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["title", "photo", "facebook_profile_link", "twitter_profile_link"]

    def clean_facebook_profile_link(self):
        fb_link = self.cleaned_data["facebook_profile_link"]
        if fb_link == "" or fb_link.startswith("https://web.facebook.com"):
            return fb_link
        else:
            raise forms.ValidationError("Not a valid facebook link.")

    def clean_twitter_profile_link(self):
        twitter_link = self.cleaned_data["twitter_profile_link"]
        if twitter_link == "" or twitter_link.startswith("https://twitter.com"):
            return twitter_link
        else:
            raise forms.ValidationError("Not a valid twitter link.")

    def clean_photo(self):
        photo = self.cleaned_data["photo"]
        if not photo or (photo.size / 2**10) <= 100:
            return photo
        else:
            raise forms.ValidationError(
                "Image size should not be larger than 100 kilobytes."
            )
