from django.urls import path

from CBV_products.apps import CbvProductsConfig
from CBV_products.views import ProductCreateView, ProductListView

app_name = CbvProductsConfig
urlpatterns = [path('', ProductListView.as_view(), name='read'),
               path('create/', ProductCreateView.as_view(), name='create')]
