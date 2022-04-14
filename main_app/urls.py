from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "Home"),
    path('about/', views.About.as_view(), name = "about"),
    path('parks/', views.ParkList.as_view(), name = "park-list")
]