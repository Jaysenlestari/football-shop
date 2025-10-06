from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

@login_required(login_url='/login/')
def show_main(request):
    products_list = Product.objects.all()
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)
        
    context = {
        "name": "Jaysen Lestari",
        "npm": "2406395335",
        "class": "PBP-C",
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login'),
        "user_id": request.user.id
    }
    return render(request, "main.html", context)

@csrf_exempt
@login_required(login_url='/login/')
def create_products(request):
    form = ProductForm(request.POST or None)

    # Jika AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.method == "POST":
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.name = strip_tags(product.name)
                product.brand = strip_tags(product.brand)
                product.description = strip_tags(product.description)
                product.save()
                return JsonResponse({
                    "status": "success",
                    "message": f"Product '{product.name}' created successfully!",
                    "redirect_url": reverse("main:show_main")
                })
            else:
                return JsonResponse({
                    "status": "error",
                    "errors": form.errors
                }, status=400)
        return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)

    return render(request, "create_products.html", {"form": form})

def show_products(request, id):
    product = get_object_or_404(Product, pk=id)
    
    context = {'product': product}
    return render(request, 'product_details.html', context)

def show_xml(request):
    products_list = Product.objects.all()
    xml_data = serializers.serialize('xml', products_list)
    return HttpResponse(xml_data, content_type='application/xml')

def show_json(request):
    products_list = Product.objects.all()
    data = [
        {
            'user_id':product.user_id,
            'id':str(product.id),
            'name':product.name,
            'price':product.price,
            'brand':product.brand,
            'description':product.description,
            'thumbnail':product.thumbnail,
            'category':product.category,
            'stock':product.stock,
            'rating':product.rating,
            'clothes_size':product.clothes_size,
            'shoe_size':product.shoe_size,
            'is_featured':product.is_featured
        }
        for product in products_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    try:
        product = Product.objects.get(pk=id)
        xml_data = serializers.serialize('xml', [product])
        return HttpResponse(xml_data, content_type='application/xml')
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, id):
    try:
        product = Product.objects.get(pk=id)
        json_data = {
            'user_id':product.user_id,
            'id':str(product.id),
            'name':product.name,
            'price':product.price,
            'brand':product.brand,
            'description':product.description,
            'thumbnail':product.thumbnail,
            'category':product.category,
            'stock':product.stock,
            'rating':product.rating,
            'clothes_size':product.clothes_size,
            'shoe_size':product.shoe_size,
            'is_featured':product.is_featured
        }
        return JsonResponse(json_data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            response_data = {
                "status": "success",
                "message": "Your account has been successfully created"
            }
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response = JsonResponse(response_data)
            else : 
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "status": "error",
                "errors": form.errors
            }, status=400)
    form = AuthenticationForm()
    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response_data = {
                "status": "success",
                "message": "Login successful",
                "redirect_url": reverse("main:show_main")
            }
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response = JsonResponse(response_data)
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))

            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "status": "error",
                "errors": form.errors
            }, status=400)

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_user(request):
    if request.method == "POST":
        logout(request)
        response = JsonResponse({
            "status": "success",
            "message": "You have been logged out successfully.",
            "redirect_url": reverse("main:login")
        })
        response.delete_cookie('last_login')
        return response
    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    }, status=405)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        p = form.save(commit=False)
        p.name = strip_tags(p.name)
        p.brand = strip_tags(p.brand)
        p.description = strip_tags(p.description)
        p.save()
        return JsonResponse({"status": "success", "message": "Product updated!"})
    return JsonResponse({"status": "error", "errors": form.errors}, status=400)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return JsonResponse({"status": "success", "message": "Product deleted!"})