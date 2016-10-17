from django.conf.urls import url
from .views import CompanyCreateView

urlpatterns = [
    url(r'^add/$', CompanyCreateView.as_view(), name='company-add'),
]
