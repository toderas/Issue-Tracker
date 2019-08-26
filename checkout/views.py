from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm, MakePaymentForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from features.models import Feature, FeatureContributors
import stripe

# Create your views here.


stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            cart = request.session.get('cart', {})
            total = 0
            for id, contribution in cart.items():
                product = get_object_or_404(Feature, pk=id)
                total += contribution 
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = contribution
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have succesfully paid")
                for id, contribution in cart.items():
                    feature = get_object_or_404(Feature, pk=id)
                    feature.value_collected += contribution
                    feature.save()
                    FeatureContributors.objects.create(post=feature, user=request.user, amount=contribution)
                    
                request.session['cart'] = {}
                return redirect(reverse('features'))
            else:
                messages.error(request, "Unable tot take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})