from django import forms
from firstapp.models import User

class form_view(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    
class NewUserform(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
