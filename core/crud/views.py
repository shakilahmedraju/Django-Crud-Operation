from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'index.html', context)

def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
        emp.save()
        return redirect('home')
    return render(request, 'index.html')

def edit(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'index.html', context)

def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
        emp.save()
        return redirect('home')
    return render(request, 'index.html')

def delete(request, id):
    emp = Employee.objects.filter(id=id)
    emp.delete()    
    return redirect('home')
