from django.urls import path
from .views import auth_view, profile_view, logout_view

urlpatterns = [
    path('', auth_view, name='auth'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
]