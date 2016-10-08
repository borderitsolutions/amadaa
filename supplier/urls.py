from django.conf.urls import url
from supplier.views import SupplierList, SupplierDetail, SupplierCreate, SupplierUpdate, SupplierDelete

urlpatterns = [
    url(r'^$', SupplierList.as_view(), name='supplier-list'),
    url(r'^detail/(?P<pk>[0-9]*)/$', SupplierDetail.as_view(),
        name='supplier-detail'),
    url(r'^add/$', SupplierCreate.as_view(), name='supplier-add'),
    url(r'^update(?P<pk>[0-9]*)/$', SupplierUpdate.as_view(), 
        name='supplier-update'),
    url(r'^delete/(?P<pk>[0-9]*)/$', SupplierDelete.as_view(), 
        name='supplier-delete'),
]
