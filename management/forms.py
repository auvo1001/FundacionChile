from django import forms
from django.contrib.admin import widgets
from management.models import Organization, User, Trip, Representative
from django.contrib.auth.models import User
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class OrganizationForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    url = forms.URLField()

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

