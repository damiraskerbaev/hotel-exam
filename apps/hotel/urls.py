from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HotelViewSet,
    home_page,
    hotel_list
)



router = DefaultRouter()
router.register('hotel', HotelViewSet, basename='hotel')


urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = [
    path('', home_page, name='home_page'),
    path('hotels/', hotel_list, name='hotel_list')
]
