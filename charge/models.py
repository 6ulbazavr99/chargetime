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

# TODO - charge
# Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAzNDQ4NTIxLCJpYXQiOjE3MDM0NDQ5MjEsImp0aSI6ImVmNDA5NjEyMTgwYzQ2Y2ZhYjYyOTIzODIyY2M4N2Q1IiwidXNlcl9pZCI6MX0.GwFFI3yU3opIyUQg9FAhGXVW74ridZG5IE0lHGAjzOg