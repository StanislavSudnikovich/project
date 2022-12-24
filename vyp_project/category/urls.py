from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone_index, name='phones'),
    path('<int:pk>/', views.phone_detail, name='phone'),
]
