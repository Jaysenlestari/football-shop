from django.forms import ModelForm
from main.models import Product, Employee

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'brand', 'description', 'thumbnail', 'category', 'is_featured', 'stock', 'clothes_size', 'shoe_size']

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["name","age","persona"]