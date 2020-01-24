from rest_framework import permissions, viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from .models import InventoryItem
from .serializers import InventoryItemSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows inventory items to be viewed and edited.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'name', 'barcode', 'qr', 'm_type', 'serial', 'room', 'brand', 'acquired']
