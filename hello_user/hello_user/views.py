# -*- coding: UTF-8 -*-

from django.shortcuts import render,render_to_response,HttpResponse,redirect
from hello_user import models
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import User

class UserForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


#def index(request):
#    people={
#        "username":"James",
#        "age":18,
#        "gender":"男" 
#    }
#    username="James"
#
#    return render(request,"index.html",{"username":username,"people":people})
   

def Login_session(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
         
            request.session['username'] = username
            return HttpResponseRedirect('/index/')
    else:
        userform = UserForm()        
    return render_to_response("login.html", {'userform':userform})

def regist(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
        
            User.objects.create(username=username,password=password)
            return HttpResponse('regist success!!')
    else:
        userform = UserForm()
    return render_to_response('regist.html',{'userform':userform})

def login(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            
            user = User.objects.filter(username__exact = username,password__exact = password)
            
            if user:
                response = HttpResponseRedirect('/success/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        userform = UserForm()
    return render_to_response('login.html',{'userform':userform})


def success(request):
    username = request.COOKIES.get('username','')
    return render_to_response('success.html', {'username':username})

def logout(request):
    response = HttpResponse('logout !!!')

    response.delete_cookie('username')
    return HttpResponse('logout ok!')   
