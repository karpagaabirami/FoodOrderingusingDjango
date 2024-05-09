from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return  render(request,'index.html')
def register(request):
    return render(request,'register.html')


def collections(request):
    catagory = Catagory.objects.all()
    return render(request,'collections.html',{"category":catagory})


def collectionparticualr(req,pk):
        cate=Catagory.objects.get(pk=pk)
        pr=product.objects.filter(Category=cate.pk)
        print(cate.name,pr)

        return render(req,'collectionparticular.html',{"cat":cate,"pr":pr})

