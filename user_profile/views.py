from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from user_profile.serializers import *
from user_profile.filters import *


class PatientProfileViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = PatientProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class DoctorProfileViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = DoctorProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class DoctorViewSet(GenericViewSet, ListModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.filter(accepted=True, role=User.ROLE_DOCTOR)
    filter_backends = [DoctorSpecializationFilterBackend]

