from django.db import models
from django.utils import timezone


class InventoryItem(models.Model):
    name = models.CharField(max_length=200, default='')
    barcode = models.IntegerField(default=0)
    qr = models.CharField('qr code', max_length=200, default='')
    m_type = models.CharField('type', max_length=200, default='')
    serial = models.CharField('serial number', max_length=200, default='')
    room = models.CharField(max_length=200, default='')
    brand = models.CharField(max_length=200, default='')
    acquired = models.DateField('date acquired', default=timezone.now)

