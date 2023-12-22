from rest_framework import viewsets
from .models import Station
from .serialiazer import StationSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
