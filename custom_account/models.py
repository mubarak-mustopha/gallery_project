from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)
    facebook_profile_link = models.URLField(blank=True)
    twitter_profile_link = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
