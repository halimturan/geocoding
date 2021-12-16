from api.models import POIEmlak
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class POIEmlakSerializer(ModelSerializer):
    class Meta:
        model = POIEmlak
        fields = '__all__'


class POIEmlakGeojsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = POIEmlak
        geo_field = "geo"
        fields = '__all__'
