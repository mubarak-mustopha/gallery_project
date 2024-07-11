from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify


# Create your models here.
class Photo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    short_title = models.CharField(max_length=15)
    slug = models.SlugField(blank=True)
    image = models.ImageField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    views = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="photos_viewed",
    )

    class Meta:
        ordering = ["-created", "-id"]

    def __str__(self):
        return self.short_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.short_title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("photo-detail", args=[self.id, self.slug])
