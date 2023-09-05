from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages

# Create your views here.

def create_product(request): 
    if request.method == 'POST':
        form = ProductForm(request.POST,request.Files)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            messages.success(request, 'THE PRODUCT CREATED')
            return redirect('/create_product/')
      
        else : 
            messages.error(request, 'THE PRODUCT NOT CREATED')

    else  :
        form =ProductForm()

    return render(request, 'create_product.html', {'form':form})
