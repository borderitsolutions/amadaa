from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from product.models import ProductCategory

# Create your views here.

class ProductCategoryList(ListView):
    model = ProductCategory
    context_object_name = 'product_categories'

class ProductCategoryDetail(DetailView):
    model = ProductCategory
    context_object_name = 'product_category'

class ProductCategoryCreate(CreateView):
    model = ProductCategory
    fields = ['name']

class ProductCategoryUpdate(UpdateView):
    model = ProductCategory
    fields = ['name']

