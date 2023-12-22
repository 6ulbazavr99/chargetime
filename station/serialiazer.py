from rest_framework import serializers
from charge.models import ChargeType
from charge.serialiazer import ColumnSerializer, ChargeTypeSerializer
from .models import StationImage, Station


class StationSerializer(serializers.ModelSerializer):
    columns = serializers.SerializerMethodField()
    charge_types = serializers.SerializerMethodField()
    capacity = serializers.SerializerMethodField()

    def get_capacity(self, obj):
        columns = obj.columns.filter(status=True)
        return columns.count()

    def get_columns(self, obj):
        columns = obj.columns.all()
        serialized_columns = ColumnSerializer(columns, many=True).data
        return serialized_columns

    def get_charge_types(self, obj):
        columns = obj.columns.all()
        charge_types = ChargeType.objects.filter(column__in=columns).distinct()
        serialized_charge_types = ChargeTypeSerializer(charge_types, many=True).data
        return serialized_charge_types

    class Meta:
        model = Station
        fields = '__all__'


class StationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationImage
        fields = '__all__'
