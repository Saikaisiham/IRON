from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password



class SellerRegistration(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    cni = models.CharField(max_length=8, blank=False, unique=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='media/seller', blank=False)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)


    def check_cni(self) -> bool:
        if (
            self.cni.isupper()
            and len(self.cni) == 8
            and self.cni[4:].isdigit()
        ):
            return True
        return False
    
    


    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        if self.password and self.confirm_password and self.password != self.confirm_password:
            raise ValidationError("Passwords don't match")

    def save(self, *args, **kwargs):
        self.clean_fields()
        if self.password and self.confirm_password:
            self.password = make_password(self.password)  
            self.confirm_password = make_password(self.confirm_password)
        super().save(*args, **kwargs)      


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"