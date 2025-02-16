from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Review, Director, Movie
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, ProductSerializer , ProductValidateSerializer, DirectorValidateSerializer
from django.db import transaction

from Afisha.movie_app.serializers import MovieValidateSerializer, ReviewValidateSerializer


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        name = serializer.validated_data.get('name')

        director = Director.objects.create(name=name)
        director.save()

        return Response(
            data={'id': director.id, 'name': director.name},
            status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_details_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorSerializer(director, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director = serializer.validated_data.get(name=director.name)
        director.save()
        return Response(
            data={'id': director.id, 'name': director.name},
            status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        movie = Movie.objects.create(title=title,
                  description=description,
                  duration=duration,
                  director_id=director_id
                  )
        movie.save()
        return Response(
        data = {'id': movie.id, 'title': movie.title},
        status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(movie, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':

        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')

        movie.save()
        return Response(
            data={'id': movie.id, 'title': movie.title},
            status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')

        review = Review.objects.create(text=text, movie_id=movie_id)

        review.save()
        return Response(data={'id': review.id, 'text': review.text}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_details_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(review, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.movie_id = serializer.validated_data.get('movie_id')

        review.save()
        return Response(data={'id': review.id, 'text': review.text}, status=status.HTTP_201_CREATED)