from django.conf.urls import url
from sales.views import manage_payment_terms
from sales.views import SalesOrderList, SalesOrderDetail, SalesOrderCreate, SalesOrderUpdate, SalesOrderDelete, QuotationList

urlpatterns = [
    url(r'^$', SalesOrderList.as_view(), name='sales-order-list'),
    url(r'^detail/(?P<pk>[0-9]*)/$', SalesOrderDetail.as_view(),
        name='sales-order-detail'),
    url(r'^add/$', SalesOrderCreate.as_view(), name='sales-order-add'),
    url(r'^update/(?P<pk>[0-9]*)/$', SalesOrderUpdate.as_view(),
        name='sales-order-update'),
    url(r'^delete/(?P<pk>[0-9]*)/$', SalesOrderDelete.as_view(),
        name="sales-order-delete"),

    url(r'^quotation/$', QuotationList.as_view(), name='quotation-list'),
    url(r'^payment-term/$', manage_payment_terms, name='payment-term-list'),
    
]
