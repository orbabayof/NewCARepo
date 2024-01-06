from django.shortcuts import render
from .models import Menu
# Create your views here.
#def menu(request):
#     newmenu = {'mains': [
#          {'name':'falafel','price':'12'},
#          {'name':'falafsdfsdel','price':'143'},
#          {'name':'faladsfsdfel','price':'2'},
#     ]}
#     return render(request,'menu.html',newmenu)

def menuByID(request):
     newmenu = { 'mains':Menu.objects.all}
     return render(request,'menuID.html',newmenu)
