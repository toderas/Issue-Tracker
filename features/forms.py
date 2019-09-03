from django import forms
from .models import Feature

class AddFeatureForm(forms.ModelForm):
    
    class Meta:
        model = Feature
        fields = ['name', 'description']
    name = forms.CharField()
    description = forms.Textarea()


class ContributeFeatureForm(forms.ModelForm):
    
    class Meta:
        model = Feature
        fields = ['amount']
    amount = forms.DecimalField(required=False,label= "Enter desired amount (min £5)", widget=forms.NumberInput(attrs={'placeholder': '£££', 'step': 1}), min_value=5)
    