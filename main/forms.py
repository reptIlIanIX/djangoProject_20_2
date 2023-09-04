from django import forms

from main.models import Product, Version


class ProductForm(forms.ModelForm):
    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'
