from django.conf.urls import url
from product.views import manage_product_categories, manage_product_types, manage_units_of_measurement, ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product-list'),
    url(r'^detail/(?P<pk>[0-9]*)/$', ProductDetail.as_view(),
        name='product-detail'),
    url(r'^add/$', ProductCreate.as_view(), name='product-add'),
    url(r'^update/(?P<pk>[0-9]*)/$', ProductUpdate.as_view(),
        name='product-update'),
    url(r'^delete/(?P<pk>[0-9]*)/$', ProductDelete.as_view(),
        name="product-delete"),

    url(r'^type/$', manage_product_types, name='product-type-list'),
    url(r'^uom/$', manage_units_of_measurement, name='uom-list'),
    url(r'category/$', manage_product_categories, name='product-category-list'),
]
