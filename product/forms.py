from django import forms
from django.forms import ModelForm
from .models import Product, PurchaseUnitOfMeasurement, SaleUnitOfMeasurement, Price
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from djmoney.forms.widgets import MoneyWidget

class ProductEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-productform'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'OK'))
        self.helper.layout = Layout(
                Div(
                    Div('name', css_class='col-xs-6'),
                    Div('internal_ref', css_class='col-xs-6'),
                    Div('item_type', css_class='col-xs-6'),
                    Div('category', css_class='col-xs-6'),
                    css_class='row_fluid'),
                Div('description', css_class='row-fluid'),
                Div(
                    Div('purchase_units_of_measurement', css_class='col-xs-6'),
                    Div('sale_units_of_measurement', css_class='col-xs-6'),
                    css_class='row-fluid'),
                )
    class Meta:
        model = Product
        exclude = []

    def save(self, commit=True):
        puoms = self.cleaned_data.pop('purchase_units_of_measurement')
        suoms = self.cleaned_data.pop('sale_units_of_measurement')
        product = super(ProductEditForm, self).save()
        for p in puoms:
            PurchaseUnitOfMeasurement.objects.create(
                    product=product,
                    unit_of_measurement=p)
        for s in suoms:
            SaleUnitOfMeasurement.objects.create(
                    product=product,
                    unit_of_measurement=s)

        return product

class PricelistForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PricelistForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['price'].label = self.instance.product

    class Meta:
        model = Price
        fields = ['price']

