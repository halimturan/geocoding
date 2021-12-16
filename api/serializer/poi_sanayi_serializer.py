from api.models import POISanayi
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class POISanayiSerializer(ModelSerializer):
    class Meta:
        model = POISanayi
        fields = '__all__'


class POISanayiGeojsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = POISanayi
        geo_field = "geo"
        fields = '__all__'
