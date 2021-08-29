from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import City, Street
from .serializers import CitySerializer, StreetSerializer


class CityViewSet(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(ReadOnlyModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
