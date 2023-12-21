from django.db import models
#from rest_framework
from ckeditor.fields import RichTextField


class ChargeType(models.Model):
    type = models.CharField(unique=True, max_length=50)
    power = models.SmallIntegerField()



class Station(models.Model):
    #charge_type = models.ManyToManyField(Charge_Type, related_name='stations')
    desc = models.TextField()
    #address
    #capacity
    name = models.CharField(max_length=255)
    schedule = RichTextField()

    #def __str__(self):




class StationImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/')
    station = models.ForeignKey(Station, related_name='images', on_delete=models.CASCADE)



class Column(models.Model):
    STATUS_CHOICES = (
        ('true', 'Свободно'),
        ('false', 'Не свободно'))
    price = models.PositiveIntegerField()
    #charge_type =
    status = models.BooleanField()


