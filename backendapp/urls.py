from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('cars/', views.CarList.as_view(), name='car_list'),
    path('cars/<int:pk>', views.CarDetail.as_view(), name='car_detail')
]