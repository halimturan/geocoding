from api.models import Mahalle
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class MahalleSerializer(ModelSerializer):
    class Meta:
        model = Mahalle
        fields = '__all__'


class MahalleGeojsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Mahalle
        geo_field = "geo"
        fields = '__all__'
