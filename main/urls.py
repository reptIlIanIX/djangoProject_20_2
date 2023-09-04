from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView, ProductDetailView, ProductDeleteView, ProductUpdateView, ProductCreateView, \
    VersionCreateView

app_name = MainConfig.name

urlpatterns = [path('', ProductListView.as_view(), name='read'),
               path('product/<int:pk>', ProductDetailView.as_view(), name='view_product'),
               path('create/', ProductCreateView.as_view(), name='create_product'),
               path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
               path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
               path('version/<int:pk>', VersionCreateView.as_view(), name='version')]
