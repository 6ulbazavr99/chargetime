from django.db import models
from ckeditor.fields import RichTextField


class StationImage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(null=True, blank=True)


class Station(models.Model):
    desc = models.TextField()
    name = models.CharField(max_length=255)
    schedule = RichTextField()
    images = models.ForeignKey(StationImage, on_delete=models.CASCADE, blank=True, null=True)
