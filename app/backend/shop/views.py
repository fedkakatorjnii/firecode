from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from django.db.models import F

from .models import Shop
from .serializers import ShopSerializer
from .filters import GeneralShopFilterBackend
from .permissions import ShopPermissions


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.annotate(street_name=F('street__name'), city_name=F('street__city__name'))
    serializer_class = ShopSerializer
    permission_classes = [ShopPermissions] 
    filter_backends = [GeneralShopFilterBackend]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_object = serializer.save()
        headers = self.get_success_headers(serializer.data)

        return Response(created_object.id, status=status.HTTP_201_CREATED, headers=headers)
