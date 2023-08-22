from django.urls import path
from main.views import home, contacts, product

urlpatterns = [path('', home),
               path('contacts/', contacts),
               path('product/<int:pk>', product)]
