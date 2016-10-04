from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from product.models import ProductCategory

# Create your views here.

class ProductCategoryList(ListView):
    model = ProductCategory
    context_object_name = 'product_categories'

class ProductCategoryDetail(DetailView):
    model = ProductCategory
    context_object_name = 'product_category'

class ProductCategoryCreate(CreateView, SuccessMessageMixin):
    model = ProductCategory
    fields = ['name']
    success_message = "Category %(name)s created"

class ProductCategoryUpdate(UpdateView, SuccessMessageMixin):
    model = ProductCategory
    fields = ['name']
    success_message = "Category %(name)s updated"

class ProductCategoryDelete(DeleteView, SuccessMessageMixin):
    model = ProductCategory
    context_object_name = 'product_category'
    success_url = reverse_lazy('product-category-list')
    success_message = "Category %(name)s removed"
