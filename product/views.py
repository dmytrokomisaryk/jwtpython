from django.shortcuts import render
from rest_framework import generics

from product.models import Product
from product.serializers import ProductSerializer

import pdb

class ProductListView(generics.ListCreateAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.request.user.products.select_related('user')

    # def post(self, request):
    #     pdb.set_trace()
        


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Product.objects.select_related('user')
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.request.user.products.select_related('user')


