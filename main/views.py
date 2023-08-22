from django.shortcuts import render

from main.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'object_list': products}
    return render(request, 'main/home.html', context)


def contacts(request):
    return render(request, 'main/contacts.html')


def product(request, pk: int):
    context = {'object_list': Product.objects.filter(id=pk)}

    return render(request, 'main/product.html', context)
