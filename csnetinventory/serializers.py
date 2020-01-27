from csnetinventory.models import InventoryItem
from rest_framework import serializers


class InventoryItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'barcode', 'qr', 'category', 'serial', 'room', 'brand', 'acquired']
