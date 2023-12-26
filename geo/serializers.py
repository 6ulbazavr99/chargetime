from rest_framework import serializers

from geo.models import Coordinates


# from geo.models import Coordinates


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['latitude', 'longitude']



class AddressSerializer(serializers.Serializer):
    address = serializers.CharField()
