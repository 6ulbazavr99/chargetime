from django.db import models
#from rest_framework
from ckeditor.fields import RichTextField



class StationImage(models.Model):
    name = models.CharField(max_length=255,  blank=True)
    image = models.ImageField(null=True, blank=True)



class ChargeTypes(models.Model):
    type = models.CharField(max_length=255)
    power = models.PositiveIntegerField()


class Column(models.Model):
    STATUS_CHOICES = (
        ('true', 'Свободно'),
        ('false', 'Не свободно'))
    price = models.PositiveIntegerField()
    charge_type = models.OneToOneField('Station.charge_type')
    status = models.BooleanField()

class Station(models.Model):
    charge_type = models.ManyToManyField(ChargeTypes, related_name='stations')
    desc = models.TextField()
    #address
    #capacity =
    columns = models.ForeignKey(Column,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    schedule = RichTextField()
    images = models.ForeignKey(StationImage, on_delete=models.CASCADE)
    #def __str__(self):












