from django import forms
from django.contrib.admin import widgets
from management.models import Organization, User, Trip, Representative
from django.contrib.auth.models import User
from functools import partial
from django.views.generic.edit import UpdateView


DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class OrganizationForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    url = forms.URLField()
    address1=forms.CharField(max_length=255)
    address2=forms.CharField(max_length=255)
    city=forms.CharField(max_length=255)
    state_province=forms.CharField(max_length=255)
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        model = Organization

class TripForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput())
    class Meta:
        model = Trip
        fields = ('date',)

class RepForm(forms.ModelForm):

    class Meta:
        model = Representative
        fields = ('FName','LName','email',)

class OrgEditForm(forms.ModelForm):
    model = Organization
    fields = ['name','country','address1','addres2','city','state_province','url',]
    template_name = 'edit_organization_form'
