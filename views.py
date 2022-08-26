from http.client import HTTPResponse
from urllib import response
from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
# Create your views here.

usr_name="alwin"
usr_password="123"
name=str

def login(request):
    if 'username' in request.session:
        if 'username' in request.COOKIES:
            if request.session['username']==request.COOKIES['username']:
                return redirect('/home')
    return render(request,'login.html')

@never_cache
def home1(request):
    if request.method=='POST': 
        name=request.POST.get('name')
        password=request.POST.get('password')    
        resp = redirect("/home")
        if usr_name==name and usr_password==password:
            resp.set_cookie('username',name)
            request.session['username']=name
            return resp
            
        
        else:
            return render(request,'login.html',{'msg':'dsdf'})
    
    else:
        return render(request,'home.html')
        
@never_cache
def home(request):
    if 'username' in request.session and 'username' in request.COOKIES:
        return render(request,'result.html',{'no':usr_name})
    
    else:
        return redirect('/')


def logout(request):

    if 'username' in request.session:
        request.session.flush()
        resp=redirect('/loginalogout')
        resp.delete_cookie('username')
        return resp


def loginpageafterlogout(request):
    return redirect('/')
    
