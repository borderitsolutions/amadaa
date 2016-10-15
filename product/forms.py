from django.forms import ModelForm
from .models import Product, PurchaseUnitOfMeasurement, SaleUnitOfMeasurement
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProductEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-productform'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'OK'))

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
