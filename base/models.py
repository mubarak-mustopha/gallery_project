from django.db import models
from django.utils.text import slugify


# Create your models here.
class Photo(models.Model):
    short_title = models.CharField(max_length=15)
    slug = models.SlugField(blank=True)
    image = models.ImageField(max_length=15)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.short_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.short_title)
        super().save(*args, **kwargs)
