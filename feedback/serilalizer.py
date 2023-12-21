from rest_framework import serializers
from .models import Review, ReviewImage, Rating


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ('id', 'image')


class ReviewSerializer(serializers.ModelSerializer):
    review_images = ReviewImageSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'review', 'author', 'station', 'review_images')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'author', 'station', 'rating')
