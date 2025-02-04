from django.contrib import admin
from movie_app.models import Review, Movie, Director

admin.site.register(Review)
admin.site.register(Director)
admin.site.register(Movie)