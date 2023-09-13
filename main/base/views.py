from django.shortcuts import render, redirect
from django.contrib.auth import logout
from products.models import Product

# Create your views here.

def base(request): 
    products = Product.objects.all()
    # print(len(products))  
    return render(request, 'base.html', {'products': products})



def logout_view(request):
    logout(request)
    return redirect('/seller/register')