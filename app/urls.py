from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetriveUpdateDestroyView
from movies.views import MovieCreateListView, MovieReatriveUpdateDestroy
from reviews.views import ReviewCreateListView, ReviewRetriveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
    
    path('actors/', ActorCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActorRetriveUpdateDestroyView.as_view(), name='actor-detail'),

    path('movies/', MovieCreateListView.as_view(), name='movie=create-list'),    
    path('movies/<int:pk>/', MovieReatriveUpdateDestroy.as_view(), name='movies-detail'),

    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),    
    path('reviews/<int:pk>/', ReviewRetriveUpdateDestroyView.as_view(), name='review-detail'),

]
