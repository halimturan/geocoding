from api.models import Kapi
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class KapiSerializer(ModelSerializer):
    class Meta:
        model = Kapi
        fields = '__all__'


class KapiGeojsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Kapi
        geo_field = "geo"
        fields = '__all__'
