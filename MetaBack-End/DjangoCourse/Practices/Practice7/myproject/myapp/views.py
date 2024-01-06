from django.shortcuts import render
from .models import Menu
from django.http import HttpResponse

# Create your views here.
def home(request):
     return render(request,'home.html',{})

def about(request):
     return render(request,'about.html',{})
def menu(request):
     newmenu = { 'mains':Menu.objects.all}
     return render(request,'menu.html',newmenu)