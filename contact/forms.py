from django import forms
from django.forms import ModelForm
from .models import Person, Organization, Membership, PhoneType, PhoneNumber, WebsiteType, Website
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit

class PersonEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
       	self.helper.layout = Layout(
       		Div(
                    Div('first_name', css_class='col-xs-2 col-lg-4'),
                    Div('last_name', css_class='col-xs-2 col-lg-4'),        
                    css_class='row_fluid input-sm'),
            
	        Div(Submit('submit', 'Add', css_class='btn btn-default'),
                   css_class='col-lg-offset-11 col-lg-4'),
        )

    class Meta:
        model = Person
        exclude = []



class OrganizationEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrganizationEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
       	self.helper.layout = Layout(
       		Div(
                    Div('name', css_class='col-xs-2 col-lg-6'),       

                    Div('members', css_class='col-xs-2 col-lg-6'),
                    css_class='row-fluid input-sm'),
            
	        Div(Submit('submit', 'Add', css_class='btn btn-default btn1'),
                   css_class='col-lg-12'),
        	)
        self.fields['members'].widget.attrs['size'] = 1
        self.fields['name'].widget.attrs['size'] = 1

    class Meta:
        model = Organization
        exclude = []

    def save(self, commit=True):
        members = self.cleaned_data.pop('members')
        organization = super(OrganizationEditForm, self).save()
        for m in members:
            Membership.objects.create(
                    organization=organization,
                    person=m)

        return organization


class PhoneNumberEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhoneNumberEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Div(
                    Div('contact', css_class='col-xs-2 col-lg-4'),
                    Div('phone_type', css_class='col-xs-2 col-lg-4'), 
                    Div('phone_number', css_class='col-xs-2 col-lg-4'),       
                    css_class='row_fluid input-sm'),
            
            Div(Submit('submit', 'Add', css_class='btn btn-default'),
                   css_class='col-lg-offset-11 col-lg-4'),
        )

    class Meta:
        model = PhoneNumber
        exclude = []


class WebsiteEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(WebsiteEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Div(
                    Div('contact', css_class='col-xs-2 col-lg-4'),
                    Div('website_type', css_class='col-xs-2 col-lg-4'), 
                    Div('url', css_class='col-xs-2 col-lg-4'),       
                    css_class='row_fluid input-sm'),
            
            Div(Submit('submit', 'Add', css_class='btn btn-default'),
                   css_class='col-lg-offset-11 col-lg-4'),
        )

    class Meta:
        model = Website
        exclude = []