from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from product.models import ProductCategory

# Create your views here.

class ProductCategoryCreate(CreateView):
    model = ProductCategory
    fields = ['name']

