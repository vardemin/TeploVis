from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from Main.models import Heater


def home(request):
    return render_to_response('base.html', context_instance=RequestContext(request))


def heater(request):
    heater_list = Heater.objects.all()
    return render_to_response('heaters.html', {'heater_list': heater_list}, context_instance=RequestContext(request))


import Main.cart as cart


def show_cart(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            cart.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            cart.update_cart(request)
    cart_items = cart.get_cart_items(request)
    page_title = 'Корзина'
    cart_subtotal = cart.cart_subtotal(request)
    return render_to_response('cart.html', locals(), context_instance=RequestContext(request))