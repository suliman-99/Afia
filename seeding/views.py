from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from seeding.models import *


class AppliedSeederViewSet(ModelViewSet):
    class AppliedSeederSerializer(serializers.ModelSerializer):
        class Meta:
            model = AppliedSeeder
            fields = ['id', 'name', 'native_name', 'code', 'is_active']
            
    serializer_class = AppliedSeederSerializer
    queryset = AppliedSeeder.objects.all()

