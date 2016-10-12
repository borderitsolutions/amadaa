from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from supplier.models import Supplier

# Create your views here.

class SupplierList(ListView):
    model = Supplier
    context_object_name = 'suppliers'

class SupplierDetail(DetailView):
    model = Supplier
    context_object_name = 'supplier'

class SupplierCreate(CreateView):
    model = Supplier
    fields = ['name']

class SupplierUpdate(UpdateView):
    model = Supplier
    fields = ['name']

class SupplierDelete(DeleteView):
    success_url = reverse_lazy('supplier-list')

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            url = success_url
            messages.success(self.request, self.cancel_message)
            return HttpResponseRedirect(url)
        else:
            messages.success(self.request, self.cancel_message)
            return super(SupplirDelete, self).delete(request, *args, **kwargs)
