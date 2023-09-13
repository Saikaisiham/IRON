from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib import messages
from seller.models import SellerRegistration
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def create_product(request): 
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            
            print("Logged-in User:", request.user)
            try:
                seller_user = get_object_or_404(SellerRegistration, user=request.user)
                print("Seller User:", seller_user)
            except SellerRegistration.DoesNotExist:
                print("Seller User not found.")

            product.owner = seller_user
            product.save()
            messages.success(request, 'THE PRODUCT CREATED')
            return redirect('/create_product/')
        else:
            messages.error(request, 'THE PRODUCT NOT CREATED')
    else:
        form = ProductForm()
    
    return render(request, 'create_product.html', {'form': form})
