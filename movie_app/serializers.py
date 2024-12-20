from rest_framework import serializers
from .models import Director, Movie, Review
from django.db.models import Avg

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source='movies.count', read_only=True)
    
    class Meta:
        model = Director
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Имя должно содержать как минимум 2 символа")
        return value


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(avg_stars=Avg('stars'))['avg_stars']
        return round(average, 2) if average else 0

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Продолжительность фильма должна быть больше 0")
        return value

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Название фильма должно быть длиной не менее 2 символов")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Рейтинг должен быть в диапазоне от 1 до 5")
        return value
