from django.urls import path
from .views import diet_view

urlpatterns = [
    path('diet/', diet_view, name='diet'),
]