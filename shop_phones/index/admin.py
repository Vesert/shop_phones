from django.contrib import admin
from . import models


admin.site.register(models.Phone)
admin.site.register(models.PhoneParameter)
admin.site.register(models.ParameterValue)
