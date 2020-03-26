from django.contrib import admin
from .models import MovieType, Movie, Review

# Register your models here.
admin.site.register(MovieType)
admin.site.register(Movie)
admin.site.register(Review)
