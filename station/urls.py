from rest_framework.routers import SimpleRouter
from station.views import StationViewSet


router = SimpleRouter()
router.register('station', StationViewSet)


urlpatterns = []
urlpatterns += router.urls
