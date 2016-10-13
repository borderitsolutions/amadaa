from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from product.models import ProductCategory, ProductType, UnitOfMeasurement, Product
from django.forms import modelformset_factory

# Create your views here.

def manage_product_categories(request):
    ProductCategoryFormSet = modelformset_factory(ProductCategory,
            can_delete=True, fields=['name',])
    if request.method == 'POST':
        formset = ProductCategoryFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse_lazy('product-list'))
    else:
        formset = ProductCategoryFormSet()
    return render(request, 'product/productcategory_manage.html', 
            {'formset': formset})

def manage_product_types(request):
    ProductTypeFormSet = modelformset_factory(ProductType,
            can_delete=True, fields=['name',])
    if request.method == 'POST':
        formset = ProductTypeFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse_lazy('product-list'))
    else:
        formset = ProductTypeFormSet()
    return render(request, 'product/producttype_manage.html',
            {'formset': formset})

def manage_units_of_measurement(request):
    UnitOfMeasurementFormSet = modelformset_factory(UnitOfMeasurement,
            can_delete=True, fields=['unit',])
    if request.method == 'POST':
        formset = UnitOfMeasurementFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse_lazy('product-list'))
    else:
        formset = UnitOfMeasurementFormSet()
    return render(request, 'product/unitofmeasurement_manage.html',
            {'formset': formset})

class ProductList(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'

class ProductCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    fields = ['name', 'internal_ref', 'product_type', 'category', 'description']
    permission_required = "product.add_product"
    raise_exception = True
    permsission_denied_message = "You do not have the permission to add products."
    success_message = "Product %(name)s created"

class ProductUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['name', 'internal_ref', 'product_type', 'category', 'description']
    permission_required = "product.change_product"
    raise_exception = True
    permission_denied_message = "You do not have the permission to update products."
    success_message = "Product %(name)s updated"

class ProductDelete(PermissionRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    permission_required = "product.delete_product"
    raise_exception = True
    permission_denied_message = "You do not have the permission to delete products."
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
