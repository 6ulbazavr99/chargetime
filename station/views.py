# import requests
from django_filters.rest_framework import DjangoFilterBackend
# from requests import Response
from rest_framework import viewsets, filters
# from rest_framework.decorators import action
# from rest_framework.response import Response

from .models import Station
from .serialiazer import StationSerializer
#   , CoordinatesSerializer, AddressSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('name', 'desc', 'schedule', )
    search_fields = ('name', 'desc', 'schedule', )

    # @action(['POST'], detail=True, serializer_class=CoordinatesSerializer)
    # def address(self, request, pk):
    #     serializer = CoordinatesSerializer(data=request.data)
    #     if serializer.is_valid():
    #         station = self.get_object()
    #         if station.address:
    #             latitude = station.address.y
    #             longitude = station.address.x
    #             api_key = ".i."
    #             base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    #             params = {'latlng': f"{latitude},{longitude}", 'key': api_key, }
    #             try:
    #                 response = requests.get(base_url, params=params)
    #                 data = response.json()
    #                 if data['status'] == 'OK':
    #                     address = data['results'][0]['formatted_address']
    #                     address_data = {'address': address}
    #                     serializer_address = AddressSerializer(data=address_data)
    #                     if serializer_address.is_valid():
    #                         return Response(serializer_address.data)
    #                     else:
    #                         return Response(serializer_address.errors, status=400)
    #                 else:
    #                     return Response({'error': 'Ошибка при получении адреса'},
    #                                     status=500)
    #             except requests.RequestException as e:
    #                 return Response({'error': 'Ошибка при запросе к API'}, status=500)
    #             except Exception as e:
    #                 return Response({'error': 'Необработанная ошибка'}, status=500)
    #         else:
    #             return Response({'error': 'Отсутствует адрес для станции'},
    #                             status=400)
    #     else:
    #         return Response(serializer.errors, status=400)
