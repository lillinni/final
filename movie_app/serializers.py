from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Director, Movie, Review
from django.db.models import Avg
import random

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.is_active = False  
        user.generate_confirmation_code()  
        user.save()
        return user


class UserConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'], confirmation_code=data['confirmation_code'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Неверное имя пользователя или код подтверждения.")
        return data

    def save(self, **kwargs):
        user = User.objects.get(username=self.validated_data['username'])
        user.is_confirmed = True  
        user.is_active = True  
        user.confirmation_code = None  
        user.save()
        return user


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
