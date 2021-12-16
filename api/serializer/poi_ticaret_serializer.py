from api.models import POITicaret
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class POITicaretSerializer(ModelSerializer):
    class Meta:
        model = POITicaret
        fields = '__all__'


class POITicaretGeojsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = POITicaret
        geo_field = "geo"
        fields = '__all__'
