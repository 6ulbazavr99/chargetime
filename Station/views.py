#################################################################################################################
############################################## adilet ###################################################################
#################################################################################################################
############################################### akylai ########################################################
#################################################################################################################

from rest_framework import viewsets, permissions
from .models import Review, ReviewImage, Rating
from .serialiazer import ReviewSerializer, ReviewImageSerializer, RatingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewImageViewSet(viewsets.ModelViewSet):
    queryset = ReviewImage.objects.all()
    serializer_class = ReviewImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
