from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from sales.models import PaymentTerm, SalesOrder
from django.forms import modelformset_factory
from .forms import SalesOrderEditForm, SalesOrderLineEditForm
# Create your views here.

@login_required
def manage_payment_terms(request):
    PaymentTermFormSet = modelformset_factory(PaymentTerm,
            can_delete=True, fields=['term',])
    if request.method == 'POST':
        formset = PaymentTermFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse_lazy('payment-term-list'))
    else:
        formset = PaymentTermFormSet()
    return render(request, 'sales/paymentterm_manage.html', 
            {'formset': formset})


class QuotationList(LoginRequiredMixin, ListView):
    context_object_name = 'sales_orders'
    queryset = SalesOrder.objects.filter(confirm_sale='Quotation')
    template_name = 'sales/quotation_list.html'

    
class SalesOrderList(LoginRequiredMixin, ListView):
    context_object_name = 'sales_orders'
    queryset = SalesOrder.objects.filter(confirm_sale='SalesOrder')

class SalesOrderDetail(LoginRequiredMixin, DetailView):
    model = SalesOrder
    context_object_name = 'sales_order'
    raise_exception = True
    success_url = reverse_lazy('sales-order-list')
    success_message = "Sales Order confirmed"
    cancel_message = "Sales confirmation cancelled"

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            url = self.success_url
            messages.success(self.request, self.cancel_message)
            return HttpResponseRedirect(url)
        else:
            url = self.success_url
            messages.success(self.request, self.success_message)
            sales_order = super(SalesOrderDetail, self).get_object()
            sales_order.confirm_sale = 'SalesOrder'
            sales_order.save()
            return HttpResponseRedirect(url)

class SalesOrderCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SalesOrder
    form_class = SalesOrderEditForm
    raise_exception = True
    success_message = "Sales Order %(customer)s created"

class SalesOrderUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SalesOrder
    form_class = SalesOrderEditForm
    # form_class = SalesOrderEditForm, SalesOrderLineEditForm
    raise_exception = True
    success_message = "Sales Order %(customer)s updated"

class SalesOrderDelete(LoginRequiredMixin, DeleteView):
    model = SalesOrder
    context_object_name = 'sales_order'
    raise_exception = True
    success_url = reverse_lazy('sales-order-list')
    success_message = "Sales Order deleted"
    cancel_message = "Delete cancelled"

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            url = self.success_url
            messages.success(self.request, self.cancel_message)
            return HttpResponseRedirect(url)
        else:
            messages.success(self.request, self.success_message)
            return super(SalesOrderDelete, self).delete(request, *args, **kwargs)