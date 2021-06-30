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

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='количество')
