from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('product/', views.ProductListAPIView.as_view(), name='product-list'),
    path('statistics/', views.StatisticsListAPIView.as_view(), name='statistics'),
    path('product/<int:pk>/', views.ProductLessonsAPIView.as_view(), name='product-lessons'),
]
