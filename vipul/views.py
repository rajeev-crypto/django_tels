from django.shortcuts import render

from django.http import HttpResponse
import datetime



def priyank(request):

    # return HttpResponse("<h1>Hello World i a mdjango </h1>")
    return render(request,'home.html',{'name':'Vipul'})

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1+ val2
    return render(request,"result.html",{'result':res})

def hello(request):
	today = datetime.datetime.now().date()
	
	return render(request,"hello.html",{"today": today,})



# Create your views here.
