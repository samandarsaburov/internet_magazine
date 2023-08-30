from django.db import models
from datetime import datetime
# Create your models here.

class ProductsModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/')
    create_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table = 'Products'
