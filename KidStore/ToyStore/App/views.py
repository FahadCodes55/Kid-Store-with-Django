from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Cart

# Create your views here.

def home(request):
    query = Item.objects.all()[:3]
    # If you have used for specific price , date use order_by('-field_name')[:2]
    return render(request, 'KidStore.html', {'items' : query})


def shop(request):
    query = Item.objects.all()
    return render(request, 'shop.html', {'items' : query})


@login_required(login_url='login')
def cart(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        try:
            quantity = int(quantity)
        except ValueError:
            quantity = 1
        total_price = item.price * quantity

        Cart.objects.create(
            user=request.user,
            item = item,
            quantity = quantity,
            total_price = total_price
        )
        return redirect('shop')

    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'carts': cart_items})


def cart_items(request):
    carts = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in carts)
    return render(request, 'cart.html', {'carts': carts, 'total_price': total_price})


def remove_cart_item(request, id):
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, pk=id)
        cart_item.delete()
        return redirect('cart_items')
    else:
        return redirect('cart_items')

def reels(request):
    return render(request, 'reels.html')
