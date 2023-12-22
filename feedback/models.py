from django.db import models

from django.contrib.auth import get_user_model

from station.models import Station

User = get_user_model()


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
    RATING_CHOICES = ((1, 'Too bad!'), (2, 'Bad!'),
                      (3, 'Normal!'), (4, 'Good!'),
                      (5, 'Excellent!'))

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_author')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_rating')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f'{self.author}'
