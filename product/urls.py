from django.conf.urls import url
from product.views import ProductCategoryList, ProductCategoryDetail, ProductCategoryCreate, ProductCategoryUpdate, ProductCategoryDelete, ProductCreate

urlpatterns = [
    url(r'add$', ProductCreate.as_view(), name='product-add'),

    url(r'^category/$', ProductCategoryList.as_view(),
        name='product-category-list'),
    url(r'^category/detail/(?P<pk>[0-9]*)/$', 
        ProductCategoryDetail.as_view(),
        name='product-category-detail'),
    url(r'^category/add$', 
        ProductCategoryCreate.as_view(), 
        name='product-category-add'),
    url(r'^category/update/(?P<pk>[0-9]*)/$',
        ProductCategoryUpdate.as_view(),
        name='product-category-update'),
    url(r'^category/delete/(?P<pk>[0-9]*)/$',
        ProductCategoryDelete.as_view(),
        name='product-category-delete'),
]
