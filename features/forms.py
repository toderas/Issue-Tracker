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
        fields = ['price']