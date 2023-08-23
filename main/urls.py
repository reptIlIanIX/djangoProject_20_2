from django.urls import path

from main.apps import MainConfig
from main.views import contacts, ProductListView, ProductDetailView

app_name = 'main'

urlpatterns = [path('', ProductListView.as_view(), name='read'),
               path('product/<int:pk>', ProductDetailView.as_view(), name='view_product')]

# path('contacts/', contacts),
