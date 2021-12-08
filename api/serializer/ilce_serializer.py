from api.models import Ilce
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class IlceSerializer(ModelSerializer):
    class Meta:
        model = Ilce
        fields = '__all__'


class IlceGeojsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ilce
        geo_field = "geo"
        fields = '__all__'
