from django.urls import path
from .views import ReverseGeocodingView

urlpatterns = [
    path('reverse-geocode/', ReverseGeocodingView.as_view(), name='reverse-geocode'),
    # Другие URL-маршруты вашего приложения...
]
