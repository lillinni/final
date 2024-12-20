from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import random

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.PositiveSmallIntegerField(default=1)  
    
    def __str__(self):
        return f'Review for {self.movie.title}'



class CustomUser(AbstractUser):
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    def generate_confirmation_code(self):
        import random
        self.confirmation_code = f"{random.randint(100000, 999999)}"
        self.save()
