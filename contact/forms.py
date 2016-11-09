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