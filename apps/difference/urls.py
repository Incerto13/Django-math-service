from django.urls import path
from . import views

urlpatterns = [
    path('difference', views.difference_view, name='difference'),
]
