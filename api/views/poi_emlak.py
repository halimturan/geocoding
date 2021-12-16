from rest_framework import viewsets, filters
from api.serializer import POIEmlakSerializer, POIEmlakGeojsonSerializer
from api.models import POIEmlak
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class POIEmlakViewSet(viewsets.ModelViewSet):
    queryset = POIEmlak.objects.all()
    serializer_class = POIEmlakSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id',)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = POIEmlak.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = POIEmlakGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)


