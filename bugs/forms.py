from django import forms
from .models import bug_item

class AddBugForm(forms.ModelForm):
    
    class Meta:
        model = bug_item
        fields = ['name', 'description']
    name = forms.CharField()
    description = forms.Textarea()
    

    