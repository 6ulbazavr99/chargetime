from django.contrib.auth import get_user_model
from django.db import models

from station.models import Station

User = get_user_model()

#dsg

class Review(models.Model):
    review = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_review')

    def __str__(self):
        return f'{self.author}: {self.review}'


class ReviewImage(models.Model):
    image = models.ImageField(upload_to='reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_image')

    def __str__(self):
        return f'{self.review.author}'


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_author')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_rating')
    rating = models.CharField(
        choices=[(i, i) for i in range(1, 6)],
        max_length=1,
    )

    def __str__(self):
        return f'{self.rating.author}'
