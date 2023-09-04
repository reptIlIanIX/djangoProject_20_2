from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from main.forms import ProductForm, VersionForm
from main.models import Product, Version


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:read')


def get_context_data(self, **kwargs):
    context_data = super().get_context_data()
    ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
    if self.request.method == 'POST':
        context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
    else:
        context_data['formset'] = ProductFormset(instance=self.object)
    return context_data


def form_valid(self, form):
    formset = self.get_context_data()['formset']
    self.object = form.save()
    if formset.is_valid():
        formset.instance = self.object
        formset.save()
    return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('main:view_product', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:read')
