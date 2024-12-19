from django.urls import path
from . import views

urlpatterns = [
    path('', views.triplet_view, name='triplet'),
]
