from django import forms
from management.models import Organization, User, Trip, Representative
from django.contrib.auth.models import User

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
    class Meta:
        model = Trip
