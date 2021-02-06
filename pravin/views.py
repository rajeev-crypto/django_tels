from django.shortcuts import render

from django.http import HttpResponse

def priyank(request):
    #return HttpResponse("Hello World i a mdjango ")
    return render(request,'index.html',{'name':'Navin'})
# Create your views here.
