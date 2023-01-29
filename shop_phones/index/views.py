from django.shortcuts import render
from django.http import HttpResponse
from .models import Phone
from django.db.models import F,Window,Subquery
from django.db.models.functions import RowNumber

def index(request):

    return HttpResponse('<body>'+'1'+'</body>')
