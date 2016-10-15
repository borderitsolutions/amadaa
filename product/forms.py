from django.forms import ModelForm
from .models import Product, PurchaseUnitOfMeasurement, SaleUnitOfMeasurement

class ProductEditForm(ModelForm):
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
