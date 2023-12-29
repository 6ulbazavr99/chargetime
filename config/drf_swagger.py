from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="chargetime API",
      default_version='v2',
      description="""
      
{
   "email": "andreypirozhkov54@gmail.com",
   "password": "bastard123",
   "password2": "bastard123",
   "first_name": "Andrey",
   "last_name": "Pirozhkov",
   "username": "andreypirozhkov54",
   "phone": "+996777123123"
}
      
   ./manage.py runserver
   redis-server
   python -m celery -A config worker -l info
   
      """,
      terms_of_service="https://www.youtube.com/watch?v=aZWWlqDy8nE",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]