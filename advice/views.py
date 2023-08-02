import random
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status
from resources.response_templates import *
from advice.serializers import *

class AdviceViewSet(GenericViewSet, ListModelMixin):

    def list(self, request, *args, **kwargs):
        advices = list(Advice.objects.all())
        random.shuffle(advices)

        short_advices = []
        meduim_advices = []
        long_advices = []

        max_short_advice_len = 90
        max_medium_advice_len = 140
        max_long_advice_len = 160

        short_advices_count = 3
        medium_advices_count = 3
        long_advices_count = 6

        for advice in advices:

            if len(advice.content) < max_short_advice_len:
                if len(short_advices) < short_advices_count:
                    short_advices.append(advice)

            elif len(advice.content) < max_medium_advice_len:
                if len(meduim_advices) < medium_advices_count:
                    meduim_advices.append(advice)

            elif len(advice.content) < max_long_advice_len:
                if len(long_advices) < long_advices_count:
                    long_advices.append(advice)

        data = {
            'short_advices': AdviceSerializer(short_advices, many=True).data,
            'meduim_advices': AdviceSerializer(meduim_advices, many=True).data,
            'long_advices': AdviceSerializer(long_advices, many=True).data,
        }

        return Response(success_response(data), status.HTTP_200_OK)

