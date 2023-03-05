from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseServerError
from django.shortcuts import render, redirect
from django.views import defaults

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)

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
