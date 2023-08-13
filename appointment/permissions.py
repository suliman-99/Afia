from rest_framework import permissions
from Auth.models import *
from appointment.models import *


class IsPatientAndOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.ROLE_PATIENT
    
    def has_object_permission(self, request, view, obj):
        return request.user == obj.patient


class IsDoctorAndOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.ROLE_DOCTOR
    
    def has_object_permission(self, request, view, obj):
        return request.user == obj.doctor


class Requested(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.status == Appointment.STATUS_REQUESTED


class Accepted(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.status == Appointment.STATUS_ACCEPTED
    
    