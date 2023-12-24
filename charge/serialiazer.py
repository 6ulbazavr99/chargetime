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
    # username = serializers.ReadOnlyField(source='request.user')
    # balance = serializers.ReadOnlyField(source='request.balance')
    # bonuses = serializers.ReadOnlyField(source='request.bonuses')

    class Meta:
        model = ChargeType
        fields = ('value', )


# class ChargeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Column
#         fields = ('price', 'status', 'station')