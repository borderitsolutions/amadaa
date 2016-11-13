from django.conf.urls import url
from contact.views import PersonList, PersonDetail, PersonCreate, PersonUpdate, PersonDelete, OrganizationList, OrganizationDetail, OrganizationCreate, OrganizationUpdate, OrganizationDelete, manage_memberships, manage_phone_types, manage_website_types, PhoneNumberList, PhoneNumberDetail, PhoneNumberCreate, PhoneNumberUpdate, PhoneNumberDelete


urlpatterns = [
    url(r'^person/$', PersonList.as_view(), name='person-list'),
    url(r'^person/detail/(?P<pk>[0-9]*)/$', PersonDetail.as_view(),
        name='person-detail'),
    url(r'^person/add/$', PersonCreate.as_view(), name='person-add'),
    url(r'^person/update/(?P<pk>[0-9]*)/$', PersonUpdate.as_view(),
        name='person-update'),
    url(r'^person/delete/(?P<pk>[0-9]*)/$', PersonDelete.as_view(),
        name="person-delete"),

    url(r'^organization/$', OrganizationList.as_view(), name='organization-list'),
    url(r'^organization/detail/(?P<pk>[0-9]*)/$', OrganizationDetail.as_view(),
        name='organization-detail'),
    url(r'^organization/add/$', OrganizationCreate.as_view(), name='organization-add'),
    url(r'^organization/update/(?P<pk>[0-9]*)/$', OrganizationUpdate.as_view(),
        name='organization-update'),
    url(r'^organization/delete/(?P<pk>[0-9]*)/$', OrganizationDelete.as_view(),
        name="organization-delete"),

    url(r'^phonenumber/$', PhoneNumberList.as_view(), name='phonenumber-list'),
    url(r'^phonenumber/detail/(?P<pk>[0-9]*)/$', PhoneNumberDetail.as_view(),
        name='phonenumber-detail'),
    url(r'^phonenumber/add/$', PhoneNumberCreate.as_view(), name='phonenumber-add'),
    url(r'^phonenumber/update/(?P<pk>[0-9]*)/$', PhoneNumberUpdate.as_view(),
        name='phonenumber-update'),
    url(r'^phonenumber/delete/(?P<pk>[0-9]*)/$', PhoneNumberDelete.as_view(),
        name="phonenumber-delete"),

    url(r'^membership/$', manage_memberships, name='membership-list'),
    url(r'^phonetype/$', manage_phone_types, name='phonetype-list'),
    url(r'^websitetype/$', manage_website_types, name='websitetype-list'),

]
