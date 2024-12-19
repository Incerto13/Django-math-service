from django.urls import path
from . import views

urlpatterns = [
    path('triplet', views.triplet_view, name='triplet'),
]
