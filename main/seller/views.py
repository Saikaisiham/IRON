from django.shortcuts import render, redirect
from .forms import SellerRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('/product')
        else:
            print(form.errors)  
    else:
        form = SellerRegistrationForm()

    return render(request, 'registration.html', {'form': form})




