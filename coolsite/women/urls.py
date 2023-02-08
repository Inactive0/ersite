from django.urls import path, re_path

from .views import *

from . import views

urlpatterns = [
    path('', index, name='home'), # осы 2 связонный хочешь просто без n или так
    path('cats/<int:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]

