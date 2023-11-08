from django.db import models
import datetime
from django.utils import timezone


class Item(models.Model):
    nome = models.TextField(max_length=100, null=True)
    upper_limit = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    lower_limit = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    frequency = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
    def is_expired(self):
        last_quoted_price = QuotedPrice.objects.filter(item=self).latest('id')
        return (last_quoted_price.created_at + datetime.timedelta(minutes=self.frequency) < timezone.now())                
    
class QuotedPrice(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    open = models.DecimalField(default=0, max_digits=20, decimal_places=6)
    high = models.DecimalField(default=0, max_digits=20, decimal_places=6)
    low = models.DecimalField(default=0, max_digits=20, decimal_places=6)
    close = models.DecimalField(default=0, max_digits=20, decimal_places=6)
    volume = models.DecimalField(default=0, max_digits=20, decimal_places=6)
    dividends = models.DecimalField(default=0, max_digits=20, decimal_places=6)
    stock_splits = models.DecimalField(default=0, max_digits=20, decimal_places=6)
        
    created_at = models.DateTimeField(auto_now=True) #hora que foi capturado

    def __str__(self):
        return self.item.nome