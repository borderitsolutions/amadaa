from django.conf.urls import url
from product.views import ProductCategoryDetail, ProductCategoryCreate

urlpatterns = [
    url(r'^category/detail/(?P<pk>[0-9]*)/$', 
        ProductCategoryDetail.as_view(),
        name='product-category-detail'),
    url(r'^category/add$', 
        ProductCategoryCreate.as_view(), 
        name='product-category-add')
]
