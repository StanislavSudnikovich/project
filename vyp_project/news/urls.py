from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_index, name='news'),
    path('<int:pk>/', views.news_detail, name='new'),
]
