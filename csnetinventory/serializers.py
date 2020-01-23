from csnetinventory.models import InventoryItem
from rest_framework import serializers

class InventoryItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['name', 'barcode', 'qr', 'm_type', 'serial', 'room', 'brand', 'acquired']
