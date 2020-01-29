import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, URLPatternsTestCase, force_authenticate

from csnetinventory.models import InventoryItem
import csnetinventory.urls


class InventoryItemTestCase(TestCase):
    def setUp(self):
        InventoryItem.objects.create(name="test 1", qr=101)
        InventoryItem.objects.create(name="test 2", qr=102)

    def test_get(self):
        item1 = InventoryItem.objects.get(name="test 1")
        item2 = InventoryItem.objects.get(name="test 2")
        self.assertEqual(item1.qr, '101')
        self.assertEqual(item2.qr, '102')


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('test_user', 'test@example.com', 'test_password')
        self.client.login(username='test_user', password='test_password')
        object1 = InventoryItem.objects.create(name="test 1", qr=101)
        object2 = InventoryItem.objects.create(name="test 2", qr=102)

        self.id1 = object1
        self.id2 = object2

    def test_get(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, [])

#
# class InventoryTestCase(APITestCase, URLPatternsTestCase):
#     urlpatterns = [
#         path('inventory/', include(csnetinventory.urls)),
#     ]
#
#     def test_create_inventory_item(self):
#         """
#         Ensure we can create a new inventory item object.
#         :return:
#         """
#         url = reverse('inventoryitem-list')
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
