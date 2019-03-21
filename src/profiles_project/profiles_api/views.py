from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format = None):
        """Returns a list of APIView features.""""

        an_apiView = [
            'Uses HTTP methads as function',
            'It is similar to a traditional Django view',
            'Gives you the most control over you logic',
            'Is mapped manually to URLs'
        ]

        return Response({ 'message': 'Hello!', 'an_apiview': an_apiview })
