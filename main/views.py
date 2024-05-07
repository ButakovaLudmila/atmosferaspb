
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def form(request):
    return render(request, 'main/form.html')

def rules(request):
    return render(request, 'main/rules.html')