from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Station
from .serialiazer import StationSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('name', 'desc', 'schedule', )
    search_fields = ('name', 'desc', 'schedule', )

    # filterset_fields = '__all__'
    # search_fields = '__all__'

# TODO - create filter for PointField(address)
