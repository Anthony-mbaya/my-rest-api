from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloAPIView(APIView):
    """tEST API VIEW"""
    serializer_class = serializers.HelloSerialzer

    def get(self, request, format=None):
        """return list of api features"""
        an_apiview = [
            'use get,post,patch,put,delete',
            'Tonny dev'
            'Gives the most control over app logic',
        ]

        return Response({'message': 'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """create hello message with name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """"handle updationg an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle particular update of object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})
