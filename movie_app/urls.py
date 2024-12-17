from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.director_list_api_view, name='director-list'),  
    path('directors/create/', views.director_list_api_view, name='director-create'),  
    path('directors/<int:id>/', views.director_detail_api_view, name='director-detail'),  
    path('directors/<int:id>/update/', views.director_detail_api_view, name='director-update'),  
    path('directors/<int:id>/delete/', views.director_detail_api_view, name='director-delete'), 
    
    path('movies/', views.movie_list_api_view, name='movie-list'),  
    path('movies/create/', views.movie_list_api_view, name='movie-create'),  
    path('movies/<int:id>/', views.movie_detail_api_view, name='movie-detail'),  
    path('movies/<int:id>/update/', views.movie_detail_api_view, name='movie-update'),  
    path('movies/<int:id>/delete/', views.movie_detail_api_view, name='movie-delete'),  

    path('reviews/', views.review_list_api_view, name='review-list'),  
    path('reviews/create/', views.review_list_api_view, name='review-create'),  
    path('reviews/<int:id>/', views.review_detail_api_view, name='review-detail'),  
    path('reviews/<int:id>/update/', views.review_detail_api_view, name='review-update'),  
    path('reviews/<int:id>/delete/', views.review_detail_api_view, name='review-delete'),  

    path('movies/reviews/', views.movie_with_reviews_api_view, name='movies-reviews'),

    path('directors/movies-count/', views.directors_with_movies_count_api_view, name='directors-movies-count'),
]
