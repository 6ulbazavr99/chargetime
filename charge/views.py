from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import ChargeHistory, UserHistory
from .models import Column, ChargeType
from .serialiazer import ColumnSerializer, ChargeTypeSerializer, ChargeSerializer

from datetime import datetime


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    @action(['POST'], detail=True, permission_classes=[IsAuthenticated], serializer_class=ChargeSerializer)
    def charge(self, request, pk):
        column = self.get_object()
        user = request.user
        balance = user.balance
        bonuses = user.bonuses
        initial_balance = balance
        history = user.history

        serializer = ChargeSerializer(data=request.data)

        if serializer.is_valid():
            value = serializer.validated_data.get('value')
            price = column.price * value

            if balance >= price:
                balance = balance - price
                user.balance = balance

                bonuses = bonuses + (price * 0.1)
                user.bonuses = bonuses

                msg = (f'({column.station.name} -> {column.charge_type}[{column.id}]) {initial_balance} - '
                       f'{price} -> {user.balance} [{user.bonuses}]')
                # now = datetime.now()
                # f_date = now.strftime("%Y-%m-%d")
                # f_time = now.strftime("%H:%M:%S")

                user_history, created = UserHistory.objects.get_or_create(user=user)

                ChargeHistory.objects.create(
                    user_history=user_history,
                    message=msg,
                    column=column,
                    station=column.station,
                    charge_type=column.charge_type
                )

                user.save()

                return Response({'msg': f'{msg}'}, status=200)

        return Response({'msg': 'There are not enough funds'}, status=400)


class ChargeTypeViewSet(viewsets.ModelViewSet):
    queryset = ChargeType.objects.all()
    serializer_class = ChargeTypeSerializer

