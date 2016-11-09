from django.conf.urls import url
from contact.views import PersonList, PersonDetail, PersonCreate, PersonUpdate, PersonDelete


urlpatterns = [
    url(r'^person/$', PersonList.as_view(), name='person-list'),
    url(r'^person/detail/(?P<pk>[0-9]*)/$', PersonDetail.as_view(),
        name='person-detail'),
    url(r'^person/add/$', PersonCreate.as_view(), name='person-add'),
    url(r'^person/update/(?P<pk>[0-9]*)/$', PersonUpdate.as_view(),
        name='person-update'),
    url(r'^person/delete/(?P<pk>[0-9]*)/$', PersonDelete.as_view(),
        name="person-delete"),

    

]
