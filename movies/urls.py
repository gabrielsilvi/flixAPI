from django.urls import path
from . import views

urlpatterns=[
    path('movies/', views.MovieCreateListView.as_view(), name='movie-create-list'),    
    path('movies/<int:pk>/', views.MovieReatriveUpdateDestroyView.as_view(), name='movie-detail'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),
]