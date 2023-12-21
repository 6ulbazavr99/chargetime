from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from Station.views import StationViewSet, ColumnViewSet, ChargeTypeViewSet

router = SimpleRouter()
router.register('station', StationViewSet)
router.register('column', ColumnViewSet)
router.register('charge-type', ChargeTypeViewSet)

urlpatterns = []
urlpatterns += router.urls
