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
from .forms import PersonEditForm, OrganizationEditForm

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



class OrganizationList(LoginRequiredMixin, ListView):
    model = Organization
    context_object_name = 'organizations'

class OrganizationDetail(LoginRequiredMixin, DetailView):
    model = Organization
    context_object_name = 'organization'

class OrganizationCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Organization
    form_class = OrganizationEditForm
    raise_exception = True
    success_message = "Organization %(name)s created"

class OrganizationUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Organization
    form_class = OrganizationEditForm
    raise_exception = True
    success_message = "Organization %(name)s updated"

class OrganizationDelete(LoginRequiredMixin, DeleteView):
    model = Organization
    context_object_name = 'organization'
    raise_exception = True
    success_url = reverse_lazy('organization-list')
    success_message = "Organization deleted"
    cancel_message = "Delete cancelled"

    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            url = self.success_url
            messages.success(self.request, self.cancel_message)
            return HttpResponseRedirect(url)
        else:
            messages.success(self.request, self.success_message)
            return super(OrganizationDelete, self).delete(request, *args, **kwargs)


@login_required
# @permission_required('contact.manage_contacts', raise_exception=True)
def manage_memberships(request):
    MembershipFormSet = modelformset_factory(Membership,
            can_delete=True, fields=['organization', 'person',])
    if request.method == 'POST':
        formset = MembershipFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse_lazy('membership-list'))
    else:
        formset = MembershipFormSet()
    return render(request, 'contact/membership_manage.html',
            {'formset': formset})


@login_required
# @permission_required('contact.manage_contacts', raise_exception=True)
def manage_phone_types(request):
    PhoneTypeFormSet = modelformset_factory(PhoneType,
            can_delete=True, fields=['phone_type',])
    if request.method == 'POST':
        formset = PhoneTypeFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse_lazy('phonetype-list'))
    else:
        formset = PhoneTypeFormSet()
    return render(request, 'contact/phonetype_manage.html',
            {'formset': formset})