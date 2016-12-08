from django import forms
from django.forms import ModelForm
from .models import Product, PurchaseUnitOfMeasurement, SaleUnitOfMeasurement, Price
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit

class ProductEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-productform'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
                Div(
                    Div('name', css_class='col-xs-2 col-lg-4'),
                    Div('internal_ref', css_class='col-xs-2 col-lg-4'),
                    Div('item_type', css_class='col-xs-2 col-lg-4'),          
                 
                    Div('category', css_class='col-xs-2 col-lg-4'),
                    Div('purchase_units_of_measurement', css_class='col-xs-2 col-lg-4'),
                    Div('sale_units_of_measurement', css_class='col-xs-2 col-lg-4'),
                    css_class='row-fluid input-sm'),
                
                Div(
                Div('description', css_class='col-xs-2 col-lg-4 input-sm'),
                css_class='textfieldsize'),


                Div(Submit('submit', 'Add', css_class='btn btn-default'),
                   css_class=' col-lg-8'),
                )

        self.fields['description'].widget.attrs['rows'] = 3
        self.fields['purchase_units_of_measurement'].widget.attrs['size'] = 2
        self.fields['sale_units_of_measurement'].widget.attrs['size'] = 2
        self.fields['category'].widget.attrs['size'] = 1


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
        fields = ['price', 'local_price']

