import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from csnetinventory.models import InventoryItem


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
        user = User.objects.create_user('test_user', 'test@example.com', 'test_password')
        self.client.login(username='test_user', password='test_password')

    def test_details(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)
