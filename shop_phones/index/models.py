from django.db import models

class Phone(models.Model):
    model_name = models.CharField(max_length=40)  



class PhonePriceHistory(models.Model):
    class Meta:
        order_with_respect_to = 'model'

    model = models.ForeignKey('Phone',on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    when_priced = models.DateTimeField(auto_now_add=True)
    is_sale_price = models.BooleanField()