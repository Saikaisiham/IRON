from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.conf import settings

user_model = settings.AUTH_USER_MODEL

class SellerRegistration    (models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    cni = models.CharField(max_length=8, blank=False, unique=True)
    email = models.EmailField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    image = models.ImageField(upload_to='media/seller', blank=False)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True ) 

    def check_cni(self) -> bool:
        if (
            self.cni.isupper()
            and len(self.cni) == 8
            and self.cni[4:].isdigit()
        ):
            return True
        return False
    

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"