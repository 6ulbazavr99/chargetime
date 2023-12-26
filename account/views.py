from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied

from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .models import ChargeHistory
from .permissions import IsUserProfile, IsUserProfileOrAdmin
from .serializers import UserSerializer, RegisterSerializer, UserProfileSerializer, ChargeHistorySerializer
from config.tasks import send_confirmation_email_task

User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer
        if self.action == 'list':
            return UserSerializer
        return UserProfileSerializer

    def get_permissions(self):
        if self.action in ('create', 'list', 'activate'):
            return [AllowAny()]
        if self.action in ('update', 'partial_update'):
            return [IsUserProfile()]
       # if self.action in ('retrieve', 'destroy'):
        return [IsUserProfileOrAdmin()]

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email_task.delay(user.email, user.activation_code)
            except Exception as e:
                return Response({'msg': 'Registered, but troubles with email!',
                                 'data': serializer.data}, status=201)
        return Response({'msg': 'Registered and sent mail!', 'data': serializer.data},
                        status=201)

    @action(['GET'], detail=False, url_path='activate/(?P<uuid>[0-9A-Fa-f-]+)')
    def activate(self, request, uuid):
        try:
            user = User.objects.get(activation_code=uuid)
        except User.DoesNotExist:
            return Response({'msg': 'Invalid link or link expired!'}, status=400)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({'msg': 'Successfully activated!'}, status=200)


class ChargeHistoryView(generics.ListAPIView):
    serializer_class = ChargeHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return ChargeHistory.objects.filter(user_history__user=user)
        else:
            raise PermissionDenied("User is not authenticated")
