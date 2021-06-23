from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='vegetables-home'),
    path('shopping/', views.shopping, name='vegetables-shopping'),
]