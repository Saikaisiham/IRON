from django.db import models
from category.models import Category
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=False, default=None)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    product_image = models.ImageField(upload_to='media/products', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    current_price = models.FloatField()
    

    def __str__(self):
        return f"{self.product_name} - {self.current_price}"
    
