from rest_framework import viewsets
from api.serializer import YolSerializer, YolGeojsonSerializer
from api.models import Yol
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_gis.filters import DistanceToPointFilter


class YolViewSet(viewsets.ModelViewSet):
    queryset = Yol.objects.all()
    serializer_class = YolSerializer
    distance_filter_field = 'geo'
    filter_backends = (DistanceToPointFilter,)

    @action(detail=False)
    def type_geojson(self, request, *args, **kwargs):
        qs = Yol.objects.all()
        queryset = self.filter_queryset(qs)
        serializer = YolGeojsonSerializer(queryset, many=True)
        return Response(serializer.data)


