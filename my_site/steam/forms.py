from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class MyFrom(forms.Form):
    name = forms.CharField(max_length=100, label='Your name', widget=forms.TextInput({'class':'hello_world','placeholder' :'Username'}))
    email = forms.EmailField(label='email', )
    message = forms.CharField(widget=forms.Textarea)

    # class Meta:
    #     fields = '__all__'
    #     widgets = {
    #         fields : forms.TextInput(attrs={'class':'hello_world'})
    #     }

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'id':'uname', }))
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Email', 'id':'email', }))
    password1 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Password', 'id':'pass1', 'type':'password' }))
    password2 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Confirm your password', 'id':'pass2', 'type':'password' }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

#
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Username', 'id':'email', }))
    password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Password', 'id':'pass1', 'type':'password' }))

    class Meta:
        model = User
        fields = ('username', 'password',)
