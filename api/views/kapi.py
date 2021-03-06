from rest_framework import viewsets, filters
from api.serializer import KapiSerializer, KapiGeojsonSerializer
from api.models import Kapi
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_gis.filters import DistanceToPointFilter
from django_filters.rest_framework import DjangoFilterBackend


class KapiViewSet(viewsets.ModelViewSet):
    queryset = Kapi.objects.all()
    serializer_class = KapiSerializer
    distance_filter_field = 'geo'
    filter_backends = (DistanceToPointFilter, DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id',)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = Kapi.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = KapiGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)
