from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView
from main.apps import MainConfig
from main.views import contacts, ProductListView, ProductDetailView

app_name = BlogConfig.name

urlpatterns = [path('', BlogListView.as_view(), name='view'),
               path('view/<int:pk>', BlogDetailView.as_view(), name='view_blog'),
               path('create/', BlogCreateView.as_view(), name='create')]
