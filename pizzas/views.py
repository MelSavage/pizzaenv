from django.shortcuts import render

from .models import Pizza

def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas."""
    pizzalist = Pizza.objects.order_by('name')
    context = {'pizzalist': pizzalist}
    return render(request, 'pizzas/pizzalist.html', context)

def toppings(request, pizza_id):
    """Show a single pizza and list all toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/toppings.html', context)
