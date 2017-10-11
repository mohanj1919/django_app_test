"""
processes the exceptions occured globally.
"""
import json
from django.http import JsonResponse
from rest_framework import status

class ExceptionMiddleware(object):
    """
    process the exceptions globally
    """

    def process_exception(self, request, exception):
        """
        processes the exception
        """
        res = {"error": True, 'content': str(exception)}
        return JsonResponse(data=res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
