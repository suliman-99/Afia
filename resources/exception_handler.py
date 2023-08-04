from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import *
from rest_framework.views import exception_handler
from resources.response_templates import *


def message_coordinator(message, field_name):
    return message \
        .replace('blank', 'null') \
        .replace('may not be null', 'is required') \
        .replace('This', field_name) \
        .replace("_id", "") \
        .replace("_", " ") \
        .capitalize() \

def get_first_error_message(detail):
    if isinstance(detail, dict):
        for key, value in detail.items():
            field_name, message = get_first_error_message(value)
            if not field_name:
                field_name = key
            return field_name, message_coordinator(message, field_name)
    if isinstance(detail, list) or isinstance(detail, tuple):
        return get_first_error_message(detail[0])
    return None, str(detail)


def get_exception_message(exc):
    try:
        return get_first_error_message(exc.detail)
    except:
        return None, str(exc)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    if response:
        status_code = response.status_code

    field_name, message = get_exception_message(exc) 

    response_data = fail_response(str(message), error_field=field_name)

    if not response:
        response = Response()

    response.status_code = status_code
    response.data = response_data

    return response

