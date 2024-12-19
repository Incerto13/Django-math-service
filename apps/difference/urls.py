from django.urls import path
from . import views

urlpatterns = [
    path('', views.difference_view, name='difference'),
]
