from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(r'shop', views.ShopViewSet, basename='shop')

urlpatterns = router.urls
