from rest_framework import viewsets
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from api.serializer import YolSerializer, YolGeojsonSerializer
from api.models import Yol
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.filters import CharFilter


class RegionFilter(GeoFilterSet):
    id = CharFilter(field_name="id")
    contains_geom = GeometryFilter(field_name="geo", lookup_expr='contains')

    class Meta:
        exclude = ('geo',)
        model = Yol


class YolViewSet(viewsets.ModelViewSet):
    queryset = Yol.objects.all()
    serializer_class = YolSerializer
    filter_class = RegionFilter

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = Yol.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = YolGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)


