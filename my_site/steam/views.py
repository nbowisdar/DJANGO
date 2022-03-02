from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class Test(ListView):
    model = 'Test'
    def get_context_data(self, *, object_list=None, **kwargs):
        super(ListView).get_context_data()


def funk(requests):
    requests.session['count'] = requests.session.get('count', 0) + 1
    return HttpResponse(f"<h1> You already was in this site {requests.session.get('count')} times</h1>"
                        f"<h3>All info about session {requests.session}"
                        f"Your requests look like - {requests.headers}")

class Test_View(TemplateView):
    extra_context = {'name': 'Vladimir', 'age': '21'}
    template_name = 'index.html'

def test_template(requests):
    context = {'name': 'Mari', 'age': '19'}

    return render(requests, 'index.html', context)

# def pattern(requests):
#     if requests.method == 'POST':
#         login, password = requests.POST['email'], requests.POST['password']
#         user = authenticate(login= login, password=password)
#         if user is not None:
#             print('Succeed login!')
#         else:
#             print('Unsucces')
#     form = LoginForm()
#
#     print(type(requests.session))
#     return render(requests, 'steam/login_page.html', {'forms':form})

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

# def register(requests):
#     if requests.method == 'POST':
#         data = requests.POST
#         user = User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
#     form = RegisterForm()
#     #form = UserCreationForm()
#     return render(requests, 'steam/register.html', {'form':form})

class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'steam/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        context['info'] = 'Create account'
        return context



class My_login(LoginView):
    template_name = 'steam/login_page.html'
    next_page = 'profile'
    authentication_form = LoginForm

    def get_context_data(self, **kwargs):
        context = super(My_login, self).get_context_data(**kwargs)
        context['title'] = 'Login_page'
        context['info'] = 'Login into your account'
        return context

def profile(requests):
    return render(requests ,'registration/profile.html', {'name':'Vladimir'})



