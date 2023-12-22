from rest_framework.routers import SimpleRouter
from feedback.views import ReviewImageViewSet, RatingViewSet


router = SimpleRouter()
router.register('review', ReviewImageViewSet)
router.register('rating', RatingViewSet)


urlpatterns = []
urlpatterns += router.urls
