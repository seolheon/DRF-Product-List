from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, FormView
from core import models, forms, filters, serializers


class ProductListView(ListView):
    template_name = 'products/plv.html'
    model = models.Product

    def get_filters(self):
        return filters.ProductFilter(self.request.GET, queryset=self.model.objects.all())

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = forms.ProductFilterForm
        context['filters'] = self.get_filters()

        return context


class ProductAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = models.Product.objects.all()
        serializer = serializers.ProductSerializer(qs, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'OK'})


class ProductModelViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    filterset_class = filters.ProductFilter
    serializer_class = serializers.ProductSerializer
