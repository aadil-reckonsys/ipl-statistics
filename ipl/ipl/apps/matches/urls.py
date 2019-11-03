from django.urls import path
from .views import MatchStatsAPI


urlpatterns = [
    path('matches/stats/<str:year>/', MatchStatsAPI.as_view(), name='match_stats')
]
