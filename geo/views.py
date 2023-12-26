from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoordinatesSerializer, AddressSerializer
import requests

class ReverseGeocodingView(APIView):
    def post(self, request):
        serializer = CoordinatesSerializer(data=request.data)
        if serializer.is_valid():
            latitude = serializer.validated_data['latitude']
            longitude = serializer.validated_data['longitude']
            api_key = "AIzaSyBO_-BjLL6YguZ4-LvlA2cmdYDdqwQ0-gs"  # Замените YOUR_API_KEY на ваш ключ API Google Geocoding

            base_url = "https://maps.googleapis.com/maps/api/geocode/json"
            params = {
                'latlng': f"{latitude},{longitude}",
                'key': api_key,
            }

            try:
                response = requests.get(base_url, params=params)
                data = response.json()

                if data['status'] == 'OK':
                    address = data['results'][0]['formatted_address']
                    address_data = {'address': address}
                    serializer = AddressSerializer(data=address_data)
                    if serializer.is_valid():
                        return Response(serializer.data)
            except Exception as e:
                return Response({'error': 'Ошибка при обратном геокодировании'}, status=500)

        return Response(serializer.errors, status=400)
