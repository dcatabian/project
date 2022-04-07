from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import loginSerializer
from .models import LoginInfo

# Create your views here.

class getLogin(APIView):
    def get(self, request, format=None):
        credentials = LoginInfo.objects.all()
        serializer = loginSerializer(credentials, many = True)
        return Response(serializer.data)

class pr(APIView):
    #def get

    #def put