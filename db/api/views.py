from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import loginSerializer
from .serializers import prSerializer
from .models import LoginInfo
from db.api import serializers

# Create your views here.

# Endpoint 1
class getLogin(APIView):
    def get(self, request, format=None):
        credentials = LoginInfo.objects.all()
        serializer = loginSerializer(credentials, many = True)
        return Response(serializer.data)

# Endpoint 2 and endpoint 8
class allpurchaseReuqest(APIView):
    def get(self, request, format = None):
        purchaseCredentials = allpurchaseReuqest.objects.all()
        serializer = allpurchaseReuqest(purchaseCredentials, many =True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = prSerializer (data = request.data)
        if serializer.is_valid( ):
            serializer.save( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # def put

# This is for endpoint 5
class allInvoices(APIView):
    def get(self, request, format = None):
        invoiceCredentials = allInvoices.objects.all()
        serializer = allInvoices(invoiceCredentials, many =True)
        return Response(serializer.data)


# This is for endpoint 6
class allItems(APIView):
    def get(self, request, format = None):
        itemCredentials = allItems.objects.all()
        serializer = allItems(itemCredentials, many =True)
        return Response(serializer.data)
