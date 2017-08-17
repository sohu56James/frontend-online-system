from django.shortcuts import render,HttpResponse,redirect
from hello_user import models

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        return HttpResponse("Hello,%s"%(username))
