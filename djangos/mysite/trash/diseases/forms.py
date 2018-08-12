from django import forms
from .models import Country

class CountryForm(forms.Form):
    #create tuples (country_code, country_name) 
    countries = Country.objects.all()
    CHOICES = ((country.country_code, country.country_name) for country in countries)
    #post = forms.CharField()
    country = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
