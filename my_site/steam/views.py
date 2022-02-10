from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
import my_site.settings as x
from .forms import *
from django.contrib.auth.models import User


context = {'name':'Mari', 'age':'19'}

def funk(requests):
    requests.session['count'] = requests.session.get('count', 0) + 1

    return HttpResponse(f"<h1> You already was in this site {requests.session.get('count')} times</h1>")

def test_template(requests):
    # d = Template(text)
    # rez = d.render(context)
    # return HttpResponse(rez)
    return render(requests, 'index.html', context)

def pattern(requests):
    form = LoginForm()

    print(type(requests.session))
    return render(requests, 'steam/login_page.html', {'forms':form})

def test_form(requests):
    if requests.method == 'POST':
        #data = requests.data
        form = MyFrom(requests.POST)
        if form.is_valid():
            #print(form)
            print(form.cleaned_data)
    else:
        form = MyFrom()
    return render(requests, 'test_form.html', {'form':form})

def register(requests):
    if requests.method == 'POST':
        data = requests.POST
        for i in data:
            print(i)
        #user = User.objects.create_user()


    form = LoginForm()
    return render(requests, 'steam/register.html', {'form':form})
