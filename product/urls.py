from django.conf.urls import url
from product.views import ProductCategoryCreate

urlpatterns = [
    url(r'^category/add$', ProductCategoryCreate.as_view(), 
        name='product-category-add')
]
