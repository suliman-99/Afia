from rest_framework.viewsets import ModelViewSet
from statics.serializers import *
from resources.filters import AllFieldsFilterBackend

class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all().select_related('country')
    filter_backends = [AllFieldsFilterBackend]


class SpecializationViewSet(ModelViewSet):
    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()

