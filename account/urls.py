from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .views import ChargeHistoryView

router = SimpleRouter()
router.register('', views.CustomUserViewSet)


urlpatterns = [
    # path('activate/<uuid:uuid>/', views.activate_user, name='activate-user'),
    path('history/', ChargeHistoryView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

] + router.urls
