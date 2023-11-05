from django.db import models

# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.symbol
    
    class Meta:
        db_table = 'master-stock'

