from rest_framework import viewsets, filters
from api.serializer import MahalleSerializer, MahalleGeojsonSerializer
from api.models import Mahalle
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class MahalleViewSet(viewsets.ModelViewSet):
    queryset = Mahalle.objects.all()
    serializer_class = MahalleSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id',)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = Mahalle.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = MahalleGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)


