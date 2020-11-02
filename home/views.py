from django.shortcuts import render, redirect,HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from .models import Wiki



# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')


def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        # check if user has entered correct credentials
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request, 'login.html')    
    

def logoutUser(request):
    logout(request)
    # Redirect to a success page.
    return redirect("/login")

def search(request):
    query=request.GET.get('search')
    info=Wiki.objects.distinct().filter(unique_source__contains=query)
    return render(request,'search.html',{'info':info})
    # return HttpResponse(qur)

def second_search(request):
    
    query=request.GET.get('search')
    info=Wiki.objects.distinct().filter(unique_source__contains=query)
    x=Wiki.objects.filter(correct=1,source=info)
    return render(request,'second_search.html',{'x':x})
    