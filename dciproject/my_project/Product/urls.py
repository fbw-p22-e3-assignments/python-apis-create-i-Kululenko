from django.urls import path
from .views import ProductList, ProductByName, ProductCreateView, ProductDeleteView

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('name/<str:name>/' , ProductByName.as_view(), name='product-by-name'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('delete/<int:product_id>/' , ProductDeleteView.as_view(), name='product-delete'),
]