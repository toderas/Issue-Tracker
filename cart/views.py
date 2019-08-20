from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart.html')
    
def add_to_cart(request, id):
    """ Add a quantity of the specified product to the cart"""
    contribution=int(request.POST.get('price'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, contribution)
    request.session['cart'] = cart
    return redirect(reverse('features'))
    
def adjust_cart(request, id):
    """ Adjust the quantity of the specified product to the specified amount"""
    contribution = int(request.POST.get('price'))
    cart = request.session.get('cart', {})
    
    if contribution > 0 :
        cart[id] = contribution
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))