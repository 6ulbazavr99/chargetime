from rest_framework import serializers
from .models import Review, ReviewImage, Rating, StationImage, Station, Column, ChargeType


class ChargeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeType
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class StationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationImage
        fields = '__all__'



#################################################################################################################
############################################## adilet ###################################################################
#################################################################################################################
############################################### akylai ########################################################
#################################################################################################################



class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    review_images = ReviewImageSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'review', 'author', 'station', 'review_images')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'author', 'station', 'rating')
