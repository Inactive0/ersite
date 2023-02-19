from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseServerError
from django.shortcuts import render, redirect
from django.views import defaults

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if (request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена 404</h1>')


def pageForbidden(reqest, exception):
    return HttpResponseForbidden('<h1>Доступ к запрошенному ресурсу запрещен 403</h1>')


def pageBadRequest(reqest, exeption):
    return HttpResponseBadRequest('<h1>Плохой запрос 400</h1>')


def pageInternalServerError(request: WSGIRequest):
    if request.path.startswith("/coolsite/"):
        return redirect("coolsite:error", error_code=500)
    elif request.path.startswith("/women/"):
        return redirect("women:error", error_code=500)
    return defaults.server_error(request)
