from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()


class StationImage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(null=True, blank=True)


class ChargeType(models.Model):
    name = models.CharField(max_length=255)
    power = models.PositiveIntegerField()


class Column(models.Model):
    price = models.PositiveIntegerField()
    station = models.ForeignKey('Station', related_name='columns', on_delete=models.CASCADE)
    charge_type = models.OneToOneField(ChargeType, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    # number = models.PositiveSmallIntegerField(unique=True)


class Station(models.Model):
    desc = models.TextField()
    name = models.CharField(max_length=255)
    schedule = RichTextField()
    images = models.ForeignKey(StationImage, on_delete=models.CASCADE, blank=True, null=True)
    # capacity = models.PositiveIntegerField()
    # charge_types = models.ManyToManyField(ChargeType, related_name='stations')


#################################################################################################################
############################################## adilet ###################################################################
#################################################################################################################
############################################### akylai ########################################################
#################################################################################################################


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












