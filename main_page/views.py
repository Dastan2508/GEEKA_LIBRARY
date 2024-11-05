from django.shortcuts import render
from django.http import HttpResponse
import datetime

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('👨‍💻Меня зовут Дастан, мне 16, хочу стать крутым программистом.💻')

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse(
            "<img src='https://avatars.mds.yandex.net/i?id=6d63867ce125a919ab022b107e452c06b62cb323eefa549e-12822619-images-thumbs&n=13'>- This is my cat, Rodrigo", )

def system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now())