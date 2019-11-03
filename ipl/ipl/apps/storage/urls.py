from django.urls import path
from .views import MatchUploadAPI, DeliveryUploadAPI


urlpatterns = [
    path('storage/match/', MatchUploadAPI.as_view(), name="match_upload"),
    path('storage/delivery/', DeliveryUploadAPI.as_view(), name="delivery_upload")
]
