from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from contact.models import Person, Organization, Membership, PhoneType, PhoneNumber, WebsiteType, Website
from django.forms import modelformset_factory
from .forms import PersonEditForm

# Create your views here.

class PersonList(LoginRequiredMixin, ListView):
    model = Person
    context_object_name = 'persons'

class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person
    context_object_name = 'person'

class PersonCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonEditForm
    raise_exception = True
    success_message = "Person %(first_name)s created"

class PersonUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Person
    form_class = PersonEditForm
    raise_exception = True
    success_message = "Person %(first_name)s updated"

class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    context_object_name = 'person'
    raise_exception = True
    success_url = reverse_lazy('person-list')
    success_message = "Person deleted"
    cancel_message = "Delete cancelled"

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            url = self.success_url
            messages.success(self.request, self.cancel_message)
            return HttpResponseRedirect(url)
        else:
            messages.success(self.request, self.success_message)
            return super(PersonDelete, self).delete(request, *args, **kwargs)