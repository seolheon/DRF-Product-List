from django import forms


class ProductFilterForm(forms.Form):
    price_min = forms.DecimalField(label='Минимальная цена', required=False, min_value=0, decimal_places=0,
                                   max_digits=10)
    price_max = forms.DecimalField(label='Максимальная цена', required=False, min_value=0, decimal_places=0,
                                   max_digits=10)
    name_contains = forms.CharField(label='Название содержит', required=False, max_length=100)
    in_stock = forms.BooleanField(label='Только в наличии', required=False)
