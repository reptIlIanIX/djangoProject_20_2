from django.shortcuts import render

from main.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'object_list': products}
    return render(request, 'main/home.html', context)


def contacts(request):
    return render(request, 'main/contacts.html')
