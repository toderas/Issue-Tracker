from django import forms
from .models import bug_item, BugComment

class AddBugForm(forms.ModelForm):
    
    class Meta:
        model = bug_item
        fields = ['name', 'description']
    name = forms.CharField()
    description = forms.Textarea()
    
    
class AddCommentForm(forms.ModelForm):
    
    class Meta:
        model = BugComment
        fields = ['comment',]
    comment = forms.Textarea()
    
class BugStatusForm(forms.ModelForm):
    class Meta:
        model = bug_item
        fields = ['status']
    status = forms.Textarea()