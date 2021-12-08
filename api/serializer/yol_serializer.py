from api.models import Yol
from rest_framework_gis.serializers import GeoFeatureModelSerializer, ModelSerializer


class YolSerializer(ModelSerializer):
    class Meta:
        model = Yol
        fields = '__all__'


class YolGeojsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Yol
        geo_field = "geo"
        fields = '__all__'
