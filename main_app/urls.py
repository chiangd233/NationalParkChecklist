from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "Home"),
    path('about/', views.About.as_view(), name = "about"),
    path('parks/', views.ParkList.as_view(), name = "park_list"),
    path('parks/new/', views.Park_Create.as_view(), name = "park_create"),
    path('parks/<int:pk>/', views.Park_Detail.as_view(), name = "park_detail"),
    path('parks/<int:pk>/update/', views.Park_Update.as_view(), name = "park_update"),
    path('parks/<int:pk>/delete/', views.Park_Delete.as_view(), name = "park_delete")
]