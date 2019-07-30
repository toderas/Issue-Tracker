from django import forms
from .models import bug_item

class AddBugForm(forms.ModelForm):
    
    class Meta:
        model = bug_item
        fields = ['name', 'description', 'in_progress']
    name = forms.CharField()
    description = forms.Textarea()
    in_progress = forms.BooleanField()
    
 