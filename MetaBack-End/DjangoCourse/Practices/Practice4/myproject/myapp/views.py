from django.shortcuts import render

# Create your views here.
def about(request):
     aboutContant = {'about': 'sdgfdgdfgdfg'}
     return render(request,'about.html',aboutContant)