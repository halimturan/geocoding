from django.contrib import admin
from django.urls import path, include

from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ilce', IlceViewSet)
router.register(r'mahalle', MahalleViewSet)
router.register(r'yol', YolViewSet)
router.register(r'kapi', KapiViewSet)
router.register(r'dini', POIDiniViewSet)
router.register(r'emlak', POIEmlakViewSet)
router.register(r'ticaret', POITicaretViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
