from rest_framework import viewsets, filters
from api.serializer import POISanayiSerializer, POISanayiGeojsonSerializer
from api.models import POISanayi
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class POISanayiViewSet(viewsets.ModelViewSet):
    queryset = POISanayi.objects.all()
    serializer_class = POISanayiSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id',)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = POISanayi.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = POISanayiGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)


