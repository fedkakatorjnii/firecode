from rest_framework import serializers

from city.models import Street

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    street = serializers.CharField(
        source='street.name')
    city = serializers.CharField(
        source='street.city.name')
    street_id = serializers.PrimaryKeyRelatedField(
        source='street',
        queryset=Street.objects.all(),
        write_only=True
    )

    class Meta:
        model = Shop
        fields = [
            'name', 'house', 'opening_time', 'closing_time', 
            'city', 'street', 'street_id'
        ]
