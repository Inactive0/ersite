from django.urls import path

from .views import *

from . import views

urlpatterns = [
    # path('', views.home, name="home"), #нет смысла включать
    path('', index), # осы 2 связонный хочешь просто без n или так
    path('cats/', categories),
]

