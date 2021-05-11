from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'), #name нужен для привязки имени ссылки в шаблон layout, при этом адрес ссылки может меняться.
    path('map', views.map, name='map'),
    path('rus_stat', views.rus_stat,name='rus_stat'),
    path('vac', views.vac,name='vac')
]
