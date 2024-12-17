from rest_framework import serializers
from .models import Director, Movie, Review
from django.db.models import Avg, Count

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source='movies.count', read_only=True)  

    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()  
    
    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(avg_stars=Avg('stars'))['avg_stars']
        return round(average, 2) if average else 0


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
