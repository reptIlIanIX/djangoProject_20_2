from django import forms

from main.models import Product, Version


class ProductForm(forms.ModelForm):
    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price',)

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')

        for item in self.forbidden_words:
            if item in cleaned_name:
                raise forms.ValidationError('Нельзя такое имя')
            return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')

        for item in self.forbidden_words:
            if item in cleaned_description:
                raise forms.ValidationError('Нельзя такое описание')
            return cleaned_description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
