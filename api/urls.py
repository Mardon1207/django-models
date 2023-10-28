from django.urls import path
from .views.product import ProductView
from .views.customer import CustomerView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>/', ProductView.as_view()),
    path('customer/', CustomerView.as_view()),
    path('customer/<int:pk>/', CustomerView.as_view()),
]