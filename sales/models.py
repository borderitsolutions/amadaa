from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from product.models import SellableItem
from customer.models import Customer
from product.models import Product, UnitOfMeasurement
from contact.models import Contact
import moneyed
from djmoney.models.fields import MoneyField

# Create your models here.

class Sale(models.Model):
    pass

class SalesLine(models.Model):
    pass

class PaymentTerm(models.Model):
    term = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.term)

class SalesOrder(models.Model):
	CONFIRM_SALE = (
	    ('Quotation', 'Quotation'),
	    ('SalesOrder', 'Sales Order'),
	)
	customer = models.ForeignKey(Contact)
	order_date = models.DateTimeField()
	payment_term = models.ForeignKey(PaymentTerm)
	products = models.ManyToManyField(Product, through='SalesOrderLine')
	note = models.TextField(blank=True, default='')
	total_price = MoneyField(max_digits=10, decimal_places=2, default_currency='GHS', default=0.0)
	confirm_sale = models.CharField(max_length=12, choices=CONFIRM_SALE, default='Quotation')
	sales_person = models.ForeignKey(User)


	def get_absolute_url(self):
		return reverse('sales-order-list')

	def __str__(self):
		return "{}".format(self.customer)


class SalesOrderLine(models.Model):
	sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	description = models.TextField(blank=True, default='')
	quantity = models.IntegerField(default=1)
	unit_price = MoneyField(max_digits=10, decimal_places=2, default_currency='GHS', default=0.0)
	unit_of_measurement = models.ForeignKey(UnitOfMeasurement)
	discount = models.PositiveIntegerField(blank=True, default=0)
	sub_total = MoneyField(max_digits=10, decimal_places=2, default_currency='GHS', default=0.0)

	def __str__(self):
		return "{}".format(self.sales_order)