from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

@api_view(['GET'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(instance=directors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def director_detail_api_view(request, id):
    director = get_object_or_404(Director, id=id)
    serializer = DirectorSerializer(instance=director)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(instance=movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = MovieSerializer(instance=movie)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(instance=reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_detail_api_view(request, id):
    review = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(instance=review)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
