from rest_framework.routers import SimpleRouter
from station.views import StationViewSet


router = SimpleRouter()
router.register('', StationViewSet)


urlpatterns = []
urlpatterns += router.urls

# path('reverse-geocode/', ReverseGeocodingView.as_view(), name='reverse-geocode'),
