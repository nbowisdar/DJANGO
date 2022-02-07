from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
import my_site.settings as x
from .forms import *


context = {'name':'Mari', 'age':'19'}

def funk(requests):
    return HttpResponse(f'<h1>{x.BASE_DIR}</h1>')

def test_template(requests):
    # d = Template(text)
    # rez = d.render(context)
    # return HttpResponse(rez)
    return render(requests, 'index.html', context)

def pattern(requests):
    form = LoginForm()
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