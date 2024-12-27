from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('users/confirm/', views.UserConfirmationView.as_view(), name='user-confirm'),

    path('directors/', views.DirectorListView.as_view(), name='director-list'),
    path('directors/create/', views.DirectorListView.as_view(), name='director-create'),
    path('directors/<int:pk>/', views.DirectorDetailView.as_view(), name='director-detail'),
    path('directors/<int:pk>/update/', views.DirectorDetailView.as_view(), name='director-update'),
    path('directors/<int:pk>/delete/', views.DirectorDetailView.as_view(), name='director-delete'),

    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movies/create/', views.MovieListView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/update/', views.MovieDetailView.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', views.MovieDetailView.as_view(), name='movie-delete'),

    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', views.ReviewListView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update/', views.ReviewDetailView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', views.ReviewDetailView.as_view(), name='review-delete'),

    path('movies/reviews/', views.MovieWithReviewsView.as_view(), name='movies-reviews'),
    path('directors/movies-count/', views.DirectorsWithMoviesCountView.as_view(), name='directors-movies-count'),
]
