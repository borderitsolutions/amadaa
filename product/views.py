from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from product.models import ProductCategory, ProductType, UnitOfMeasurement, Product

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
    permission_required = 'product.change_productcategory'
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

class ProductTypeList(ListView):
    model = ProductType
    context_object_name = 'product_types'

class ProductTypeDetail(DetailView):
    model = ProductType
    context_object_name = 'product_types'

class ProductTypeCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = ProductType
    fields = ['name']
    permission_required = "product.add_producttype"
    raise_exception = True
    permission_denied_message = "You do not have the permission to add product types."
    success_message = "Product type %(name)s created"

class ProductTypeUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ProductType
    fields = ['name']
    permission_required = "product.change_producttype"
    raise_exception = True
    permission_denied_message = "You do not have the permission to update prodcut types."
    success_message = "Product type %(name)s updated"

class ProductTypeDelete(PermissionRequiredMixin, DeleteView):
    model = ProductType
    context_object_name = 'product_type'
    permission_required = "product.delete_producttype"
    raise_exception = True
    permission_denied_message = "You do not have the permission to delete product types."
    success_url = reverse_lazy('product-type-list')
    success_message = 'Product type deleted'
    cancel_message = 'Delete cancelled'

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            messages.success(self.request, self.cancel_message)
            return HttpResponseRedirect(self.success_url)
        else:
            messages.success(self.request, self.success_message)
            return super(ProductTypeDelete, self).delete(request, *args,
                    **kwargs)

class UnitOfMeasurementList(ListView):
    model = UnitOfMeasurement
    context_object_name = 'uoms'

class UnitOfMeasurementDetail(DetailView):
    model = UnitOfMeasurement
    context_object_name = 'uom'

class UnitOfMeasurementCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = UnitOfMeasurement
    fields = ['unit']
    permission_required = "product.add_unitofmeasurement"
    raise_exception = True
    permission_denied_message = "You do not have the permission to add units of measurement."
    success_message = "Unit of measurement %(unit)s created"

class UnitOfMeasurementUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UnitOfMeasurement
    fields = ['unit']
    permission_required = "product.change_unitofmeasurement"
    raise_exception = True
    permission_denied_message = "You do not have the permission to change units of measurement."
    success_message = "Unit of measurement %(unit)s updated"

class UnitOfMeasurementDelete(PermissionRequiredMixin, DeleteView):
    model = UnitOfMeasurement
    context_object_name = 'uom'
    permission_required = "product.delete_unitofmeasurement"
    raise_exception = True
    permission_denied_message = "You do not have the permission to delete units of measurement."
    success_url = reverse_lazy('uom-list')
    success_message = "Unit of measurement removed"
    cancel_message = "Delete cancelled"

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            messages.success(self.request, self.cancel_message)
            return HttpResponseRedirect(self.success_url)
        else:
            messages.success(self.request, self.success_message)
            return super(UnitOfMeasurementDelete, self).delete(request,
                    *args, **kwargs)

class ProductList(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'

class ProductCreate(SuccessMessageMixin, CreateView):
    model = Product
    fields = ['name', 'internal_ref', 'product_type', 'category', 'description']
    success_message = "Product %(name)s created"

class ProductUpdate(SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['name', 'internal_ref', 'product_type', 'category', 'description']
    success_message = "Product %(name)s updated"

class ProductDelete(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product-list')
    success_message = "Product deleted"
    cancel_message = "Delete cancelled"

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            url = self.success_url
            messages.success(self.request, self.cancel_message)
            return HttpResponseRedirect(url)
        else:
            messages.success(self.request, self.success_message)
            return super(ProductDelete, self).delete(request, *args, **kwargs)
