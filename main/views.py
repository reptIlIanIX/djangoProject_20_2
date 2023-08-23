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


# def product(request, pk: int):
#     context = {'object_list': Product.objects.filter(id=pk)}
#
#     return render(request, 'main/product.html', context)
