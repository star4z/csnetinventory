from django.http import HttpResponse
from django.shortcuts import render

from django.views import generic

from django.core import serializers

from .models import InventoryItem


def index(request):
    data = serializers.serialize("json", InventoryItem.objects.all())
    return HttpResponse(data)

def update(request, item):
    
    pass
