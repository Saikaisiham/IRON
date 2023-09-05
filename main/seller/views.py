from django.shortcuts import render, redirect
from .models import SellerRegistration
from .forms import SellerRegistrationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('/')
        else:
            print(form.errors)  
    else:
        form = SellerRegistrationForm()

    return render(request, 'registration.html', {'form': form})

