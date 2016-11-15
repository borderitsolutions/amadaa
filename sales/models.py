from django.db import models
from product.models import SellableItem
from customer.models import Customer
from product.models import Product

# Create your models here.

class Sale(models.Model):
    pass

class SalesLine(models.Model):
    pass

class PaymentTerm(models.Model):
    term = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.term)

class SalesOrder(Product):
	CONFIRM_SALE = (
	    ('Quotation', 'Quotation'),
	    ('SalesOrder', 'Sales Order'),
	)
	customer = models.ForeignKey(Customer)
	order_date = models.DateTimeField()
	payment_term = models.ForeignKey(PaymentTerm)
	confirm_sale = models.CharField(max_length=12, choices=CONFIRM_SALE,default='Quotation')


	def get_absolute_url(self):
		return reverse('sales-order-list')

	def __str__(self):
		return "{}".format(self.customer)