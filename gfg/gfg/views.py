from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from gfg1.models import Entrepreneur
from gfg1.models import Funders
from gfg1.models import Donaters

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

#for project function
#Crud operations
def project(request):
    emp = Entrepreneur.objects.all()

    context ={
        'emp' : emp,
    }
    return render(request,"project.html",context)

def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Entrepreneur(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('project')

    return render(request,'project.html')

# edit operation
def EDIT(request):
    emp = Entrepreneur.objects.all()

    context ={
        'emp' : emp,
    }
    return redirect(request,'project.html',context)

#update operation
def Update(request,id):
    if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       address= request.POST.get('address')
       phone= request.POST.get('phone')

       emp = Entrepreneur(
        id=id,
        name = name,
        email = email,
        address = address,
        phone = phone,
       )
       emp.save()

       return redirect('project')

    return redirect(request,'project.html')

# delete operation

def delete(request,id):
    emp = Entrepreneur.objects.filter(id=id)
    emp.delete()
    

    context = {
        'emp' : emp,
    }
    return redirect('project')
    

#for managing the inovative ideas
def inovate(request):
    ino = Funders.objects.all()

    context ={
        'ino' : ino,
    }
    return render(request,'inn.html',context)


#for donation

def Donate(request):
    return render(request,'donate.html')


#for funding
def Fund(request):
    return render(request,'fund.html')

#adding the donation to the table
def addamt(request):
    if request.method == 'POST':
        funder = request.POST.get('funder')
        city = request.POST.get('city')
        amount = request.POST.get('amount')

        add=Donaters(
            Funder = funder,
            City = city,
            amount = amount
        )

        add.save()

     
        return redirect('donaters1')

    return redirect(request,'fund')      

def donaters1(request):
    org = Donaters.objects.all()

    context ={
        'org' : org
    }
    return render(request,'funders.html',context)


def view(request):

    emp = Entrepreneur.objects.all()
    context ={
        'emp':emp
    }
    return render (request,'view.html',context)


def payment(request):
    return render(request,'payment.html')


def addvalue(request):
    if request.method == 'POST':
        Funder = request.POST.get('Funder')
        Inovater = request.POST.get('Inovater')
        Idea = request.POST.get('Idea')
        Amount = request.POST.get('Amount')

        fund = Funders(
            name=Funder,
            email = Inovater,
            patent = Idea,
            phone = Amount,

        )

        fund.save()

       
        return redirect('inovate')
    
    return render(request,'payment.html')

 