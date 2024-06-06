from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """tEST API VIEW"""

    def get(self, request, format=None):
        """return list of api features"""
        an_apiview = [
            'use get,post,patch,put,delete',
            'Tonny dev'
            'Gives the most control over app logic',
        ]

        return Response({'message': 'Hello', 'an_apiview':an_apiview})
