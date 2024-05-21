from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListView, ProductModelViewSet, ProductAPIView


app_name = 'core'

router = DefaultRouter()
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('plv/', ProductListView.as_view(), name='plv'),
    path('papiv/', ProductAPIView.as_view(), name='papiv'),
    path('pmvs/', include(router.urls)),
]

