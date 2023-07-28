import json
from rest_framework.response import Response
from resources.response_templates import *


class ResponseCoordinatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response:Response = self.get_response(request)
        
        if request.path.startswith('/__debug__'):
            return response
        
        try:
            response_data = json.loads(response.content)

            if 200 <= response.status_code < 300:
                if not TEMPLATE_FLAG in response_data:
                    response_data = success_response(response_data)

            response_data.pop(TEMPLATE_FLAG)

            response.content = json.dumps(response_data)

        except:
            pass

        return response
