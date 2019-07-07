from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import DateTimeField


class Order(models.Model):
    BUY = ('BUY', 'BUY')
    SELL = ('SELL', 'SELL')
    ORDER_TYPE = [BUY, SELL]

    OPEN = ('OPEN', 'OPEN')
    CLOSE = ('CLOSE', 'CLOSE')

    ORDER_STATUS = [OPEN, CLOSE]

    order_id = models.AutoField
    order_timestamp = DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    order_symbol = models.CharField(max_length=15)
    order_type = models.CharField(choices=ORDER_TYPE, max_length=15)
    order_quantity = models.PositiveIntegerField()
    order_price = models.DecimalField(validators=[MinValueValidator(0.00)], max_digits=16, decimal_places=2)
    order_status = models.CharField(choices=ORDER_STATUS, max_length=15)
