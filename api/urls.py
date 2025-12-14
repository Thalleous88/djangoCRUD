from django.urls import path
from .views import ProductListCreate, ProductDetailView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    # Product endpoints
    path("products/", ProductListCreate.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),
    # Schema and Documentation endpoints
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema')),
]