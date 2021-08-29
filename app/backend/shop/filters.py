from django.db.models import Q
from django.utils.datetime_safe import  datetime
from rest_framework import filters

from city.models import City, Street


class GeneralShopFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        street = request.query_params.get('street')
        city = request.query_params.get('city')
        open = request.query_params.get('open')

        params = Q()

        if street is not None:
            new_params = Q(street_id=street)
            
            params.add(new_params, Q.AND)
        if city is not None:
            streets = Street.objects.filter(city_id=city)
            street_id = [street.id for street in streets]
            new_params = Q(street_id__in=street_id)

            params.add(new_params, Q.AND)
        if open is not None:
            time = datetime.now().strftime("%H:%m:%S")

            if open == '1':
                new_params = Q(opening_time__lte=time, closing_time__gte=time)
                params.add(new_params, Q.AND)
            elif open == '0':
                new_params = Q(opening_time__gte=time, closing_time__lte=time)
                params.add(new_params, Q.AND)

        # print('params', params)
        return queryset.filter(params)
