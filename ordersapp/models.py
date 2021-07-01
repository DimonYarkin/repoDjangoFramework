from django.conf import settings
from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RD'
    DELIVERED = 'DVD'
    CANCEL = 'CNC'

    STATUSES = (
        (FORMING, 'Формируется'),
        (SEND_TO_PROCEED, 'Обрабатывается'),
        (PROCEEDED, 'Обработан'),
        (PAID, 'Оплачен'),
        (READY, 'Готов к выдаче'),
        (DELIVERED, 'Выдан'),
        (CANCEL, 'Отменен'),

    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='обнавлен')
    is_active = models.BooleanField(default=True)

    status = models.CharField(choices=STATUSES, default=FORMING, verbose_name='статус')

    def get_total_quantity(self):
        _items = self.orderitems.select_related()
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    def get_total_cost(self):
        _items = self.orderitems.select_related()
        _totalquantity = sum(list(map(lambda x: x.get_product_cost(), _items)))
        return _totalquantity


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='количество')

    def get_product_cost(self):
        return self.product.price * self.product.quantity