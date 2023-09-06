from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


# Create your views here.
class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        quaryset = super().get_queryset()
        quaryset = quaryset.filter(is_published=True)
        return quaryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('topic', 'description', 'image', 'date_start', 'is_published')
    success_url = reverse_lazy('blog:view')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.topic)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('topic', 'description', 'image', 'date_start', 'is_published')

    def get_success_url(self):
        return reverse('blog:view_blog', args=[self.object.id])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:view')

