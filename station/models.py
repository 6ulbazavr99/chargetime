from django.contrib.gis.db import models
from ckeditor.fields import RichTextField

# class Coordinates(models.Model):
#     latitude = models.FloatField()
#     longitude = models.FloatField()
# #     # station = models.
# #
#     def __str__(self):
#         return f"Latitude: {self.latitude}, Longitude: {self.longitude}"



class StationImage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.image}"

class Station(models.Model):
    desc = models.TextField()
    name = models.CharField(max_length=255)
    schedule = RichTextField()
    images = models.ForeignKey(StationImage, on_delete=models.CASCADE, blank=True, null=True)
    address = models.PointField()

    def __str__(self):
        return f'{self.name} ({self.address})'
