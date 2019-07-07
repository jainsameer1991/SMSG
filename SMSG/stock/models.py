from django.core.validators import MinValueValidator
from django.db import models
# Create your models here.

class Stock(models.Model):
    stock_id = models.AutoField
    stock_symbol = models.CharField(max_length=15)
    stock_name = models.CharField(max_length=255)
    stock_price = models.DecimalField(validators=[MinValueValidator(0.00)], max_digits=16, decimal_places=2)