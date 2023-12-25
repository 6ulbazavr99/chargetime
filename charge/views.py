from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Column, ChargeType
from .serialiazer import ColumnSerializer, ChargeTypeSerializer, ChargeSerializer


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    @action(['POST'], detail=True, permission_classes=[IsAuthenticated], serializer_class=ChargeSerializer)
    def charge(self, request, pk):
        column = self.get_object()
        user = request.user
        balance = user.balance
        bonuses = user.bonuses

        serializer = ChargeSerializer(data=request.data)

        if serializer.is_valid():
            value = serializer.validated_data.get('value')
            price = column.price * value

            if balance >= price:
                balance = balance - price
                user.balance = balance

                bonuses = bonuses + (price * 0.1)
                user.bonuses = bonuses

                user.save()

                return Response({'msg': f'-{price} -> {user.balance} [{user.bonuses}]'}, status=200)

        return Response({'msg': 'There are not enough funds'}, status=400)


class ChargeTypeViewSet(viewsets.ModelViewSet):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer

