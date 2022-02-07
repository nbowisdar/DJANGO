from django import forms

class MyFrom(forms.Form):
    name = forms.CharField(max_length=100, label='Your name', widget=forms.TextInput({'class':'hello_world','placeholder' :'Username'}))
    email = forms.EmailField(label='email', )
    message = forms.CharField(widget=forms.Textarea)

    # class Meta:
    #     fields = '__all__'
    #     widgets = {
    #         fields : forms.TextInput(attrs={'class':'hello_world'})
    #     }

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Username', 'id':'uname'}))
    password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Password', 'id':'pass'}))

