from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import BookModel
# Create your views here.
@csrf_exempt
def BookView(request):
     if request.method == 'GET':
          books = BookModel.objects.all().values()
          books_list = list(books)
          return JsonResponse({'books':books_list},status = 200)
     elif request.method == 'POST':
          title = request.POST.get('title')
          author = request.POST.get('author')
          price = request.POST.get('price')
          inventory = request.POST.get('inventory')
          book = BookModel(title=title,author=author,price=price,inventory=inventory)
          try:
               book.save()
          except IntegrityError:
               return JsonResponse({'error':'true','message':'required field missing'},status=400)
          return JsonResponse(model_to_dict(book),status = 201)
