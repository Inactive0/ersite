from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения women.")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")

def home(request):
    return render(request, 'home.html')

def error_404(request, exeption):
    return render(request, '404.html')