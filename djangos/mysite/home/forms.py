from django import forms

class HomeForm(forms.Form):
    CHOICES = (('USA', 'America',), ('CMR', 'Cameroon',))
    post = forms.CharField()
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
