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
        fields = ['comment', ]
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class EditBugForm(forms.ModelForm):

    class Meta:
        model = bug_item
        fields = ['name', 'description']
    name = forms.CharField()
    description = forms.Textarea()
