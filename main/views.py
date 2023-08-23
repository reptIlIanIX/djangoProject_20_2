from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product.html'

def contacts(request):
    return render(request, 'main/contacts.html')


