from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductByName(generics.ListAPIView):
    serializer_class = ProductSerializer
   
    def get_queryset(self):
        name = self.kwargs['name']
        return Product.objects.filter(product_name=name)


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


@TokenAuthentication #want to try as decoraters
@IsAuthenticated
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_id'
  