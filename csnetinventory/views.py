from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.core import serializers

from rest_framework import viewsets

from .models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows inventory items to be viewed and edited.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
