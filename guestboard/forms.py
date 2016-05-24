from django import forms
from .models import Posting


class PostingForm(forms.ModelForm):
    
    class Meta:
        model = Posting
        fields = ('name', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'size': 40}),
            'message': forms.Textarea(attrs={'cols': 80, 'rows': 20})
            }
        
