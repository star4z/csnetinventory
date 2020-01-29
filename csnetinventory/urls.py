from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'inventory'

router = routers.DefaultRouter()
router.register('', views.InventoryItemViewSet, basename='inventory')

urlpatterns = [
    path('', include(router.urls))
]