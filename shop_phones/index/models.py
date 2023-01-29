from django.db import models

class Phone(models.Model):
    model_name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    is_sale_price = models.BooleanField(default=False)

class PhoneParameter(models.Model):
    name_parameter = models.CharField(max_length=40)
    phone = models.ManyToManyField('Phone',through='ParameterValue')

class ParameterValue(models.Model):
    phone_parameter = models.ForeignKey('PhoneParameter', on_delete= models.CASCADE)
    phone = models.ForeignKey('Phone', on_delete= models.CASCADE)
    parameter_value = models.CharField(max_length=100)
    