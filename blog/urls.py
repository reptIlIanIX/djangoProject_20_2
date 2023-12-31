from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView

# from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


app_name = BlogConfig.name

urlpatterns = [path('', BlogListView.as_view(), name='view'),
               path('view/<int:pk>', BlogDetailView.as_view(), name='view_blog'),
               path('create/', BlogCreateView.as_view(), name='create'),
               path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit_blog'),
               path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete')]
