from api.models import POIDini
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class POIDiniSerializer(ModelSerializer):
    class Meta:
        model = POIDini
        fields = '__all__'


class POIDiniGeojsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = POIDini
        geo_field = "geo"
        fields = '__all__'
