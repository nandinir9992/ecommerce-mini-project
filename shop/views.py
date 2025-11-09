from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, Order, ShippingAddress
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email', '')
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Signup successful! Please login.")
            return redirect('login_view')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
    item.save()
    return redirect('view_cart')


def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = sum(i.product.price * i.quantity for i in items)
    return render(request, 'cart.html', {'items': items, 'total': total})


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart')


def update_quantity(request, item_id, action):
    item = get_object_or_404(CartItem, id=item_id)
    if action == 'increase':
        item.quantity += 1
    elif action == 'decrease' and item.quantity > 1:
        item.quantity -= 1
    item.save()
    return redirect('view_cart')


def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = sum(i.product.price * i.quantity for i in items)

    if request.method == 'POST':
        address = request.POST['address']
        city = request.POST['city']
        postal = request.POST['postal']
        country = request.POST['country']
        order = Order.objects.create(user=request.user, total=total)
        ShippingAddress.objects.create(order=order, address=address, city=city, postal_code=postal, country=country)
        items.delete()  # clear cart
        return render(request, 'order_summary.html', {'order': order})

    return render(request, 'checkout.html', {'items': items, 'total': total})



