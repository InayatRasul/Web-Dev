from django.contrib import admin
from django.urls import path
from api.views import show_products, show_product, show_categories, show_category, show_category_product

urlpatterns = [
    path('products/', show_products),
    path('products/<int:product_id>/',show_product ),
    path('categories/', show_categories ),
    path('categories/<int:id>/', show_category),
    path('categories/<int:id>/products', show_category_product  ),
]