from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MovieType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='movietype'
        verbose_name_plural='movietypes'
    
class Movie(models.Model):
    moviename=models.CharField(max_length=255)
    movietype=models.ForeignKey(MovieType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    movieprice=models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    movieentrydate=models.DateField()
    movieurl=models.URLField(null=True, blank=True)
    moviedescription=models.TextField()

    def __str__(self):
        return self.moviename
    
    class Meta:
        db_table='movie'
        verbose_name_plural='movies'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table='review'
        verbose_name_plural='reviews'
    
