import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ("jersey","Jersey"),
        ("shoes","Shoes"),
        ("socks","Socks"),
        ("accessories","Accessories"),
    ]
    
    CLOTHES_SIZES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    SHOE_SIZES = [
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    stock = models.IntegerField()
    rating = models.FloatField(default=0.0)
    clothes_size = models.CharField(max_length=5, choices=CLOTHES_SIZES, blank=True, null=True)
    shoe_size = models.CharField(max_length=5, choices=SHOE_SIZES, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_products_reccomended(self):
        return self.rating >= 4.5