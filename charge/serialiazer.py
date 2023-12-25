from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Column, ChargeType


User = get_user_model()


class ChargeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeType
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'


class ChargeSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField()

    class Meta:
        model = ChargeType
        fields = ('value', )
