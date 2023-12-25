from django.db import models

from station.models import Station


class ChargeType(models.Model):
    name = models.CharField(max_length=255)
    power = models.PositiveIntegerField()


class Column(models.Model):
    price = models.PositiveIntegerField()
    station = models.ForeignKey(Station, related_name='columns', on_delete=models.CASCADE)
    charge_type = models.OneToOneField(ChargeType, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
