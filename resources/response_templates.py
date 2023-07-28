from django.utils.translation import gettext_lazy as _

TEMPLATE_FLAG = '_______#IS_TEMPLATE#_______'

def response_template(data, message, error_field):
    return {
        'message': str(_(message)),
        'error_field': error_field,
        'data': data,
        TEMPLATE_FLAG: True,
    }


def success_response(data, message='Success'):
    return response_template(data, message, None)


def fail_response(message='Fail', error_field=None):
    return response_template(None, message, error_field)

