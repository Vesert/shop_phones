from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F,Window,Subquery
from django.db.models.functions import RowNumber
from .models import Phone,ParameterValue,PhoneParameter
from django.core.paginator import Paginator


def index(request):
    page_number = request.GET.get('page')
    context = {'phones':Paginator(Phone.objects.all(),10).get_page(page_number)}
    return HttpResponse(render(request,'index/index.html',context=context))

def detail(request,phone_id):
    phone_info = Phone.objects.get(pk=phone_id)
    phone_parameters = ( {'parameter_name':i.phone_parameter.name_parameter,
                          'parameter_value':i.parameter_value} 
                        for i in ParameterValue.objects.select_related('phone_parameter').filter(phone=phone_id))
    context = {'phone_name': phone_info.model_name,
               'phone_price':phone_info.price,
               'phone_parameters': phone_parameters}
    
    return HttpResponse(render(request,'index/detail.html',context=context))

    
