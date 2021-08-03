from django.test import TestCase
from django.test.client import Client
from products.models import Product, ProductCategory
from django.core.management import call_command


class TestProductsSmoke(TestCase):
    success = 200

    def setUp(self):
        self.client = Client()
        cat_1 = ProductCategory.objects.create(name='cat_1')
        cat_2 = ProductCategory.objects.create(name='cat_2')
        Product.objects.create(name='prod_1', price=999.99, category=cat_1, image='products_images/Adidas-hoodie.png')
        Product.objects.create(name='prod_2', price=1999.99, category=cat_2, image='products_images/Adidas-hoodie.png')

    def test_products_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.success)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, self.success)

        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/{category.pk}/')
            self.assertEqual(response.status_code, self.success)

    def tearDown(self):
        call_command('sqlsequencereset', 'products', 'users', 'orders', 'baskets')
