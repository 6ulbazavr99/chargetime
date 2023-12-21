from django.db import models
from ckeditor.fields import RichTextField


class StationImage(models.Model):
    name = models.CharField(max_length=255,  blank=True)
    image = models.ImageField(null=True, blank=True)


class ChargeType(models.Model):
    type = models.CharField(max_length=255)
    power = models.PositiveIntegerField()


class Column(models.Model):
    STATUS_CHOICES = (
        ('true', 'Свободно'),
        ('false', 'Не свободно'))
    price = models.PositiveIntegerField()
    # charge_type = models.OneToOneField('Station.charge_types', on_delete=models.CASCADE, related_name='columns')
    status = models.BooleanField()


class Station(models.Model):
    charge_types = models.ManyToManyField(ChargeType, related_name='stations')
    desc = models.TextField()
    # columns = models.ForeignKey(Column,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    schedule = RichTextField()
    images = models.ForeignKey(StationImage, on_delete=models.CASCADE)
    #address
    #capacity =
    #def __str__(self):


#################################################################################################################
############################################## adilet ###################################################################
#################################################################################################################
############################################### akylai ########################################################
#################################################################################################################


from django.contrib.auth import get_user_model
from django.db import models

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_author')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_rating')
    rating = models.CharField(
        choices=[(i, i) for i in range(1, 6)],
        max_length=1,
    )

    def __str__(self):
        return f'{self.rating.author}'












