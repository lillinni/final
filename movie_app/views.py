from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Avg, Count
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


@api_view(['GET'])
def movie_with_reviews_api_view(request):
    movies = Movie.objects.annotate(average_rating=Avg('reviews__stars')) 
    data = []

    for movie in movies:
        reviews = movie.reviews.all()
        review_serializer = ReviewSerializer(reviews, many=True)
        data.append({
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'duration': movie.duration,
            'average_rating': round(movie.average_rating, 2) if movie.average_rating else 0,
            'reviews': review_serializer.data
        })

    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def directors_with_movies_count_api_view(request):

    directors = Director.objects.annotate(movies_count=Count('movies'))
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
