from rest_framework import viewsets, filters
from api.serializer import POITicaretSerializer, POITicaretGeojsonSerializer
from api.models import POITicaret
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class POITicaretViewSet(viewsets.ModelViewSet):
    queryset = POITicaret.objects.all()
    serializer_class = POITicaretSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id',)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = POITicaret.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = POITicaretGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)


