from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from product.models import ProductCategory, Product

# Create your views here.

class ProductCategoryList(ListView):
    model = ProductCategory
    context_object_name = 'product_categories'

class ProductCategoryDetail(DetailView):
    model = ProductCategory
    context_object_name = 'product_category'

class ProductCategoryCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = ProductCategory
    fields = ['name']
    permission_required = 'product.add_productcategory'
    raise_exception = True
    permission_denied_message = "You do not have the permission to add product categories"
    success_message = "Category %(name)s created"

class ProductCategoryUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ProductCategory
    fields = ['name']
    permission_required = 'product.edit_productcategory'
    raise_exception = True
    permission_denied_message = "You do not have the permission to modify product categories"
    success_message = "Category %(name)s updated"

class ProductCategoryDelete(PermissionRequiredMixin, DeleteView):
    model = ProductCategory
    context_object_name = 'product_category'
    permission_required = 'product.delete_productcategory'
    raise_exception = True
    permission_denied_message = "You do not have the permission to delete product categories"
    success_url = reverse_lazy('product-category-list')
    success_message = "Category removed"
    cancel_message = "Removal cancelled"

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.success_url
            messages.warning(self.request, self.cancel_message)
            return HttpResponseRedirect(url)
        else:
            messages.success(self.request, self.success_message)
            return super(ProductCategoryDelete, self).delete(request, 
                    *args, **kwargs)

class ProductList(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'internal_ref', 'category']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'internal_ref', 'category']

class ProductDelete(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            url = self.success_url
            return HttpResponseRedirect(url)
        else:
            return super(ProductDelete, self).delete(request, *args, **kwargs)
