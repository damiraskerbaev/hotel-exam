from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginPage, my_booking, SignupView, logout_view

from .views import GuestViewSet

router = DefaultRouter()
router.register('guest', GuestViewSet, basename='guest')

urlpatterns = [
    path('', include(router.urls)),

    path('profile/', my_booking, name='my_booking'),
    path('login/', LoginPage, name='LoginPage'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout')
]