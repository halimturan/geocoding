from rest_framework import viewsets, filters
from api.serializer import POIDiniSerializer, POIDiniGeojsonSerializer
from api.models import POIDini
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class POIDiniViewSet(viewsets.ModelViewSet):
    queryset = POIDini.objects.all()
    serializer_class = POIDiniSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id',)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = POIDini.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = POIDiniGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)


