from rest_framework import viewsets
from api.serializer import MahalleSerializer, MahalleGeojsonSerializer
from api.models import Mahalle
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.filters import CharFilter
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter


class RegionFilter(GeoFilterSet):
    id = CharFilter(field_name="id")
    contains_geom = GeometryFilter(field_name="geo", lookup_expr='contains')

    class Meta:
        exclude = ('geo',)
        model = Mahalle


class MahalleViewSet(viewsets.ModelViewSet):
    queryset = Mahalle.objects.all()
    serializer_class = MahalleSerializer
    filter_class = RegionFilter

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = Mahalle.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = MahalleGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)
