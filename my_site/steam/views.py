from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def funk(requests):
    return HttpResponse('I get this')

def pattern(requests):
    return render(requests, 'index.html')
