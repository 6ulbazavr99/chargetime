from rest_framework.routers import SimpleRouter
from charge.views import ColumnViewSet, ChargeTypeViewSet


router = SimpleRouter()
router.register('column', ColumnViewSet)
router.register('charge-type', ChargeTypeViewSet)


urlpatterns = []
urlpatterns += router.urls
