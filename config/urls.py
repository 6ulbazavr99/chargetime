from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .drf_swagger import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/station/', include('station.urls')),
    path('api/v1/charge/', include('charge.urls')),
    path('api/v1/feedback/', include('feedback.urls')),
    path('api/v1/geo/', include('geo.urls')),

]

urlpatterns += doc_urls  # swagger docs urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
