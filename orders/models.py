from django.db import models
from datetime import datetime
# Create your models here.

class OrderModel(models.Model):
    name = models.CharField('Name', max_length=10)
    tel = models.CharField(max_length=20)
    yashash_joyi = models.CharField(max_length=100)
    order_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'order'
