from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from product.models import ProductCategory, ProductType, UnitOfMeasurement, Product, PurchaseUnitOfMeasurement, SaleUnitOfMeasurement, Price
from django.forms import modelformset_factory
from .forms import ProductEditForm, PricelistForm

# Create your views here.

@login_required
@permission_required('products.manage_products', raise_exception=True)
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

@login_required
@permission_required('products.manage_products', raise_exception=True)
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

@login_required
@permission_required('products.manage_products', raise_exception=True)
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

class ProductList(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'

class ProductCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductEditForm
    permission_required = "product.manage_products"
    raise_exception = True
    permsission_denied_message = "You do not have the permission to add products."
    success_message = "Product %(name)s created"

class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    permission_required = "product.manage_products"
    raise_exception = True
    permission_denied_message = "You do not have the permission to update products."
    success_message = "Product %(name)s updated"

class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    permission_required = "product.manage_products"
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

def manage_pricelist(request):
    PriceFormSet = modelformset_factory(Price, form=PricelistForm, extra=0)
    if request.method == 'POST':
        formset = PriceFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse_lazy('product-list'))
    else:
        for uom in SaleUnitOfMeasurement.objects.all():
            try:
                Price.objects.create(product=uom, price=0.0, local_price=0.0)
            except:
                pass
        formset = PriceFormSet()
    return render(request, 'product/pricelist_manage.html',
            {'formset': formset})
