from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated and not(request.user.is_staff):

        return  render(request,'index.html')
    else:
        return redirect('login')
def register(request):
    return render(request,'register.html')


def collections(request):
    catagory = Catagory.objects.all()
    return render(request,'collections.html',{"category":catagory})


def collectionparticualr(req,pk):
        cate=Catagory.objects.get(pk=pk)
        pr=product.objects.filter(Category=cate.pk)
        print(cate.name,cate.pk,pr)

        return render(req,'collectionparticular.html',{"cat":cate,"pr":pr})


from .forms import *
from .models import *

def customer(req):
    if req.method=='POST':
        form=customerform(req.POST)
        if form.is_valid():
            custo=form.save(commit=False)
            email=form.cleaned_data['Emailid']
            password=form.cleaned_data['phoneno']
            user=User.objects.create_user(username=email,email=email,password=password)
            custo.user=user
            custo.save()
            return redirect('home')
    else:
        form=customerform()
    return render(req,'customer.html',{'form':form})

from django.contrib.auth import *
def custlogin(req):
    if req.user.is_authenticated and not(req.user.is_staff):
        return redirect("home")
    if req.method=="POST":
        form=custologin(req.POST)
        if form.is_valid():
            user=form.cleaned_data['Emailid']
            passw = form.cleaned_data['phoneno']
            user=authenticate(req,username=user,password=passw)
            if user is not None:
                login(req,user)
                return redirect("home")
            else:
                form.add_error(None,'Invalid')
    else:
        form=custologin()
    return render(req,'login.html',{'form':form})

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def ulog(req):
    logout(req)
    return redirect('login')