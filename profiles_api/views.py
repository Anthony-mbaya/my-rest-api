from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


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


class HelloViewSet(viewsets.ViewSet):
    """test api viewsets"""
    serializer_class = serializers.HelloSerialzer
    def list(self, request):
        """Return hello message"""
        a_viewset = [
        'list,create,retrieve,update,partial_update',
        'Tonny',
        'Mbaya',
        'Crux',
        ]
        return Response({'message':'welcome','a_viewset':a_viewset})

    def create(self, request):
        """ceate new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """handle updating"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """partial update"""
        return Response({'http_method':'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'http_method':'DELETE'})
