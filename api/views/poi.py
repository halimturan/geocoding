from rest_framework import viewsets, filters
from api.serializer import POISerializer, POIGeojsonSerializer
from api.models import POI
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class POIViewSet(viewsets.ModelViewSet):
    queryset = POI.objects.all()
    serializer_class = POISerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id',)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = POI.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = POIGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)


