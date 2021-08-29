from django.db import models
from rest_framework import serializers

from city.models import Street

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()
    street = serializers.SerializerMethodField()
    street_id = serializers.PrimaryKeyRelatedField(
        source='street',
        queryset=Street.objects.all(),
        write_only=True
    )

    class Meta:
        model = Shop
        fields = [
            'name', 'house', 'opening_time', 'closing_time', 
            'city', 'street', 'street_id', 
        ]

    def get_street(self, obj):
        return obj.street.name

    def get_city(self, obj):
        return obj.street.city.name
    

