from django import forms

class MyFrom(forms.Form):
    name = forms.CharField(max_length=100, label='Your name')
    email = forms.EmailField(label='email')
    message = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget={})