from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from CBV_products.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'main/base.html'
class ProductCreateView(CreateView):
    model = Product
    fields = ('first_name', 'description')

