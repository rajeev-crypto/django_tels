from django.shortcuts import render

from django.http import HttpResponse

def priyank(request):
    #return HttpResponse("Hello World i a mdjango ")
    return render(request,'index.html',{'name':'Navin'})

def add(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val1+ val2
    return render(request,"result.html",{'result':res})


# Create your views here.
