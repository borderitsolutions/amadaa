from django.conf.urls import url
from .views import CompanyUpdate

urlpatterns = [
    url(r'^add/$', CompanyCreate.as_view(), name='company-add'),
    url(r'^update/(?P<pk>[0-9]*)/$', CompanyUpdate.as_view(),
        name='company-update'),
]
