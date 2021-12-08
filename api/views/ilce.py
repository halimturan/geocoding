from rest_framework import viewsets, filters
from api.serializer import IlceSerializer, IlceGeojsonSerializer
from api.models import Ilce
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class IlceViewSet(viewsets.ModelViewSet):
    queryset = Ilce.objects.all()
    serializer_class = IlceSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('id',)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = Ilce.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = IlceGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)


