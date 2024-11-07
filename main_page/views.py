from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models


# film_list
def books_list_view(request):
    if request.method == 'GET':
        film_list = models.Books.objects.filter().order_by('-id')
        context = {'book_list': film_list}
        return render(request, template_name='book.html', context=context)


# detail film
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)









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