from django.urls import path
from .views import workout_view

urlpatterns = [
    path('workout/', workout_view, name='workout'),
]