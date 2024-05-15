from django.shortcuts import render, redirect
from .manage import OrderForm, FurnitureForm, CreateCustomerForm
from django.forms import inlineformset_factory
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import json
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    furniture = Furniture.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    delivered = orders.filter(status='Delivered').count()

    context = {
        'furniture': furniture, 'customers': customers, 'orders': orders, 'delivered': delivered
    }

    return render(request, 'store/home.html', context)

def manage(request):
    furniture = Furniture.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'furniture':furniture, 'customers':customers, 'orders': orders,
        'delivered':delivered, 'pending':pending
    }

    return render(request, 'store/manage.html', context)

def furniture(request):
    furniture = Furniture.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'furniture':furniture, 'customers':customers, 'orders': orders, 'delivered':delivered, 'pending':pending
    }

    return render(request, 'store/furniture.html', context)

def contact(request):
    return render(request, 'store/contact.html')


def update_furniture(request, name):
    furniture = Furniture.objects.get(name=name)
    form = FurnitureForm(instance=furniture)
    if request.method == 'POST':
        form = FurnitureForm(request.POST, instance=furniture)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'store/order_form.html', context)

def delete_furniture(request, name):
    furniture = Furniture.objects.get(name=name)
    if request.method == 'POST':
        furniture.delete()
        return redirect('/')
    context = {'item': furniture}
    return render(request, 'store/delete.html',context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'store/order_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'store/delete.html',context)

def create_customer(request):
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'store/create_customer.html', context)


def create_furniture(request):
    form = FurnitureForm()
    if request.method == 'POST':
        form = FurnitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'store/create_customer.html',context)

#do it same as add furniture
def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'store/create_order.html',context)
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request,'store/register.html',context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username =username,password =password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'user or password not correct!')

    context={}
    return render(request,'store/login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')

def cart(request):
    return render(request,'store/cart.html')
def ordersucces(request):
    return render(request,'store/ordersucces.html')