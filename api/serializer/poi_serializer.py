from api.models import POI
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class POISerializer(ModelSerializer):
    class Meta:
        model = POI
        fields = '__all__'


class POIGeojsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = POI
        geo_field = "geo"
        fields = '__all__'
