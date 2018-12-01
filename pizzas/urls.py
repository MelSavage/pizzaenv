"""Defines URL patterns for pizzas."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all pizzas.
    url(r'^pizzas/$', views.pizzas, name='pizzalist'),

    # List toppings for a single pizza.
    url(r'^pizzas/(?P<pizza_id>\d+)/$', views.toppings, name='toppings'),
]
