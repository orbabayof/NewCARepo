from django.shortcuts import render
from django.http import HttpResponse

from menuapp.forms import Form
# Create your views here.
def formView(request):
     form = Form()
     if request.method == 'POST':
          form = Form(request.POST)
          if form.is_valid():
               form.save()
     context = {"form":form}
     return render(request , 'home.html',context)