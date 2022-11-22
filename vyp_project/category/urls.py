from django.urls import path
from . import views

urlpatterns = [
    path('', views.phones, name='phones'),
    path('<int:pk>/', views.phone, name='phone'),
]
