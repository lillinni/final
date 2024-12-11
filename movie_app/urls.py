from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.director_list_api_view, name='director-list'),
    path('directors/<int:id>/', views.director_detail_api_view, name='director-detail'),
    path('movies/', views.movie_list_api_view, name='movie-list'),
    path('movies/<int:id>/', views.movie_detail_api_view, name='movie-detail'),
    path('reviews/', views.review_list_api_view, name='review-list'),
    path('reviews/<int:id>/', views.review_detail_api_view, name='review-detail'),
]
