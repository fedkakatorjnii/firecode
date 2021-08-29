from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(r'city', views.CityViewSet, basename='city')
router.register(r'street', views.StreetViewSet, basename='street')

urlpatterns = router.urls
