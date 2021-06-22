from django.db import models

from users.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def total_quantity(self):
        user_basket = Basket.objects.filter(user=self.user)
        return sum([i.quantity for i in user_basket])

    def total_price(self):
        user_basket = Basket.objects.filter(user=self.user)
        return sum([i.sum() for i in user_basket])
