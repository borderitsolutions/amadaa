from django.conf.urls import url
from contact.views import PersonList, PersonDetail, PersonCreate, PersonUpdate, PersonDelete, OrganizationList, OrganizationDetail, OrganizationCreate, OrganizationUpdate, OrganizationDelete, manage_memberships, manage_phone_types


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

    url(r'^membership/$', manage_memberships, name='membership-list'),
    url(r'^phonetype/$', manage_phone_types, name='phonetype-list'),

]
