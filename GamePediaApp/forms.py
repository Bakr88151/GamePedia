from django import forms
from .models import genres

pubs =['CDProjectRed', 'Ubisoft', 'konami', 'Activision', 'Square Enix', 'Electronic Arts ', 'Epic Games']
devs = ['CDProjectRed', 'Ubisoft', 'konami', 'Activision', 'Square Enix', 'Electronic Arts ', 'Epic Games']

class New_Game_Form(forms.Form):
    title = forms.CharField(max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'mysuperform', 'autocomplete': 'off'}))
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'mysuperform', 'autocomplete': 'off'}))
    description = forms.CharField(required=True, max_length=4096, widget=forms.Textarea(attrs={'class': 'mysuperform', 'autocomplete': 'off'}))
    release_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': 'mysuperform', 'type': 'date',  'autocomplete': 'off'}))
    genres =forms.CharField(required=True ,widget=forms.Select(choices=[(genres.index(genre)+1, genre) for genre in genres], attrs={'multiple': True, 'class': 'mysuperformselect', 'required': True}), label='Genres (Hold CTRL to select multiple):')
    dev = forms.CharField(required=True,widget=forms.TextInput(attrs={ 'class': 'mysuperform', 'type': 'text', 'autocomplete': 'off'}), label='Developer:')
    pub = forms.CharField(required=True,widget=forms.TextInput(attrs={ 'class': 'mysuperform', 'type': 'text', 'autocomplete': 'off'}), label='Publisher:')


class Review_Form(forms.Form):
    rating = forms.FloatField(max_value=10, min_value=0, required=True, widget=forms.NumberInput(attrs={'class': 'rating_input'}))
    review = forms.CharField(max_length=4096, required=False, widget=forms.Textarea(attrs={'class': 'rating_review'}))