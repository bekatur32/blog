from django import forms
from .models import comment

class EmailPostForms(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name', 'email', 'body']

class Searchforms(forms.Form):
    query = forms.CharField()