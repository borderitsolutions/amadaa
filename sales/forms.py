from django import forms
from django.forms import ModelForm
from .models import SalesOrder, SalesOrderLine
from product.models import Product, Price, SaleUnitOfMeasurement
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from decimal import Decimal
from django.forms.models import inlineformset_factory


class SalesOrderEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SalesOrderEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-productform'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
                Div(
                    Div('customer', css_class='col-xs-2 col-lg-4'),
                    Div('order_date', css_class='col-xs-2 col-lg-4 datepicker'),
                    Div('payment_term', css_class='col-xs-2 col-lg-4'),
                    Div('sales_person', css_class='col-xs-2 col-lg-4'),          
                    css_class='row_fluid input-sm'),
                
                
                Div(
                Div('note', css_class='col-xs-2 col-lg-4 input-sm'),
                css_class='textfieldsize'),
                Div(Submit('submit', 'Add', css_class='btn btn-default'),
                   css_class='col-lg-offset-11 col-lg-4'),
                )

        self.fields['note'].widget.attrs['rows'] = 2


    class Meta:
        model = SalesOrder
        exclude = ['confirm_sale', 'total_price', 'products']

    # def save(self, commit=True):
    #     products = self.cleaned_data.pop('products')
    #     total = 0
    #     for product in products:
    #         suom = SaleUnitOfMeasurement.objects.get(product=product)
    #         product_price = Price.objects.get(product=suom)
    #         total = total + product_price.price
    #     sales_order = super(SalesOrderEditForm, self).save()
    #     sales_order.products = products 
    #     sales_order.total_price = total
    #     sales_order.save()
            
    #     return sales_order



class SalesOrderLineEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SalesOrderLineEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-productform'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
                Div(
                    Div('product', css_class='col-xs-2 col-lg-4'),
                    css_class='row-fluid input-sm'),
                
                Div(
                Div('description', css_class='col-xs-2 col-lg-4 input-sm'),
                css_class='textfieldsize'))

        self.fields['description'].widget.attrs['rows'] = 1


    class Meta:
        model = SalesOrderLine
        exclude = ['sub_total', 'sales_order']


SOLFormSet = inlineformset_factory(SalesOrder, SalesOrderLine, SalesOrderLineEditForm, extra=2)