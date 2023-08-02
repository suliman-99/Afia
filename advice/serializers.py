from rest_framework import serializers
from advice.models import *


class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = ['id', 'content']

