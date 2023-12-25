import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Station
from .serialiazer import StationSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    # filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']