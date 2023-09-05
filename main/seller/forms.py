from django import forms
from django.contrib.auth.hashers import make_password
from .models import SellerRegistration

class SellerRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        max_length=128, 
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(),
        help_text="Enter the same password as above, for verification."
    )

    class Meta:
        model = SellerRegistration
        fields = '__all__'

   