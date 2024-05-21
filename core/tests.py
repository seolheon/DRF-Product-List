from rest_framework.test import APITestCase
from core.models import Product

class ProductModelViewSetTests(APITestCase):
    def setUp(self):
        self.product_data = {
            'name': 'Test Product',
            'price': 10,
            'stock': 20
        }
        self.product = Product.objects.create(**self.product_data)
        self.list_url = '/pmvs/products/'
        self.detail_url = f'/pmvs/products/{self.product.pk}/'

    def test_post(self):
        response = self.client.post(self.list_url, self.product_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 2)

    def test_get_all(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_details(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.product_data['name'])

    def test_put(self):
        updated_data = {'name': 'Updated Product', 'price': 150, 'stock': 25}
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, updated_data['name'])

    def test_patch(self):
        updated_data = {'price': 20}
        response = self.client.patch(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, updated_data['price'])

    def test_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)
