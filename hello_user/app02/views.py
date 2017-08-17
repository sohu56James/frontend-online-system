#-*- coding:utf-8 -*-

from django.shortcuts import render
from app02 import models
#from models import Tb2

# Create your views here.
def index(request):
    people={
        "username":"James",
        "age":18,
        "gender":"男" 
    }
    username="James"

    return render(request,"index.html",{"username":username,"people":people})
