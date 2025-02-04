from rest_framework import serializers
from movie_app.models import Review, Director, Movie

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields='text'.split()

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields='name'.split()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields='title description duration'.split()