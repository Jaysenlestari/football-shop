from django import forms
from django.utils.html import strip_tags
from main.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'brand', 'description', 'thumbnail',
            'category', 'is_featured', 'stock', 'clothes_size', 'shoe_size'
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        return strip_tags(name)

    def clean_brand(self):
        brand = self.cleaned_data.get('brand', '')
        return strip_tags(brand)

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        return strip_tags(description)
