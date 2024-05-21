import django_filters

from core import models

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Название содержит', lookup_expr='icontains')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Стоимость до')
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Стоимость от')

    in_stock = django_filters.BooleanFilter(label='В наличии', method='filter_in_stock')

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        if 'in_stock' in self.data and self.data['in_stock'] == 'True':
            queryset = self.filter_in_stock(queryset, 'in_stock', True)
        return queryset

    class Meta:
        model = models.Product
        fields = ['name', 'price_to', 'price_from', 'in_stock']