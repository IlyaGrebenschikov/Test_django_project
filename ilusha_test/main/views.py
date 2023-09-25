from django.shortcuts import render
import requests
import time


def index(request):
    data = {
        'title': 'Главная страница',

    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'Про нас',
    }
    return render(request, 'main/about.html', data)


def contacts(request):
   data = {
       'title': 'Связь с нами',
   }
   return render(request, 'main/contacts.html', data)