from django.http import HttpResponse

from .forms import UPbike
from . models import New_bikes
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    bikes=New_bikes.objects.all()
    data={
        "values":bikes
    }
    return  render(request,"index.html",data)

def details(request,bike_num):
    bike=New_bikes.objects.get(id=bike_num)

    return render(request,'details.html',{"bike":bike})

def add_bike(request):
    if request.method=='POST':
        name=request.POST.get('name')
        brand=request.POST.get('brand')
        price=request.POST.get('price')
        img=request.FILES['img']
        bike=New_bikes(name=name,brand=brand,price=price,img=img)
        bike.save()
    return render(request,'add.html')

def update(request,id):
    bike=New_bikes.objects.get(id=id)
    form=UPbike(request.POST or None,request.FILES,instance=bike)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return  render(request,'update.html',{'form':form,'bike':bike})

def delete(request,id):
    if request.method=='POST':
        bike=New_bikes.objects.get(id=id)
        bike.delete()
        return  redirect('/')
    return render(request,'delete.html')