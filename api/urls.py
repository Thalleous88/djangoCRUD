from django.urls import path
from .views import ProductListCreate, ProductDetailView

urlpatterns = [
    path("products/", ProductListCreate.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view())
]