from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request,'index.html')


def signup(request):

    if request.method =="POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['Email']
        pass1 = request.POST['Pass1']
        pass2 = request.POST['Pass2']

        #now we are creating the some extra condition in login
        if User.objects.filter(username=username):
            messages.error(request,"User Name already exists")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"Email already exists")
            return redirect('home')

        if len(username)>10:
            messages.error(request,"username length must within 10 ")

        if pass1 != pass2:
            messages.error(request,"Password didn't match!")

        if not username.isalnum():
            messages.error(request,"username must be alpha numeric")
            return redirect('home')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        
        messages.success(request,"Your account has been succesfully created." )

        return redirect('signin')


    return render(request,"signup.html")

def signin(request):

    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['Pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"index.html",{'fname':fname})
     
        else:
            messages.error(request,"Bad Credential")
            return  redirect('home')

    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully ")
    return redirect('home')
