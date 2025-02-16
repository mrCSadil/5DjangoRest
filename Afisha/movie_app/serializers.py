from rest_framework import serializers
from movie_app.models import Review, Director, Movie
from rest_framework.exceptions import ValidationError

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

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=True, max_length=500)
    duration = serializers.IntegerField(min_value=1)
    director = DirectorValidateSerializer(many=True, min_value=1, required=False)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError("Director does not exist")
        return director_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)
    movie = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError("Movie does not exist")
        return movie_id