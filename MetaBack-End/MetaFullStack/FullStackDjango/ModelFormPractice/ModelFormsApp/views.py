from django.shortcuts import render
from .forms import LoggerForm
from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import Logger
# Create your views here.
class FormView(View):
     def get(self,request):
          form = LoggerForm()
          context = {'form':form}
          return render(request,"log.html",context)
     def post(self,request):
          form = LoggerForm(request.POST)
          if form.is_valid():
            form.save()
            return HttpResponse('success')  # Redirect to a success page
          else:
            context = {'form': form}
            return render(request, "log.html", context)
          
def FormJSview(request):
     form = LoggerForm()
     if request.method == 'POST':
        
        form = LoggerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uc = Logger(
                username = cd['username'],
                password = cd['password'],
            )
            return JsonResponse({'message': 'success'})
     return render(request,'log2.html',{'form':form})
   
