from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from product.models import ProductCategory

# Create your views here.

class ProductCategoryList(ListView):
    model = ProductCategory
    context_object_name = 'product_categories'

class ProductCategoryDetail(DetailView):
    model = ProductCategory
    context_object_name = 'product_category'

class ProductCategoryCreate(SuccessMessageMixin, CreateView):
    model = ProductCategory
    fields = ['name']
    success_message = "Category %(name)s created"

class ProductCategoryUpdate(SuccessMessageMixin, UpdateView):
    model = ProductCategory
    fields = ['name']
    success_message = "Category %(name)s updated"

class ProductCategoryDelete(DeleteView):
    model = ProductCategory
    context_object_name = 'product_category'
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

