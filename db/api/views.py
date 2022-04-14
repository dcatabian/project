from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import invoiceSerializer, itemSerializer, loginSerializer, prSerializer
from .models import Invoice, LoginInfo, Member, PurchaseRequest, Item
#from db.api import serializers

# Create your views here.

# Endpoint 1
class getLogin(APIView):
    
    def get(self, request, uname, format=None):
        credentials = LoginInfo.objects.filter(username = uname)
        serializer = loginSerializer(credentials, many = True)
        return Response(serializer.data)

# Endpoint 2 and endpoint 8
class allpurchaseRequest(APIView):
    def get(self, request, format = None):
        purchaseCredentials = PurchaseRequest.objects.all()
        serializer = prSerializer(purchaseCredentials, many =True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = prSerializer (data = request.data)
        if serializer.is_valid( ):
            serializer.save( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # def put
# endpoint 3

class userPurchaseRequest(APIView):
    def get(self, request, u, format = None):
        user = Member.objects.get(pk=u)
        theirs = PurchaseRequest.objects.filter(sub_id = user)
        serializer = prSerializer(theirs)
        return Response(serializer.data)

# This is for endpoint 4

# class UserPurchaseRequestID(APIView):
#     def get(self, request, pk, format = None):

 

# This is for endpoint 5 and endpoint 9
class allInvoices(APIView):
    def get(self, request, format = None):
        invoiceCredentials = Invoice.objects.all()
        serializer = invoiceSerializer(invoiceCredentials, many =True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = invoiceSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# This is for endpoint 6
class allItems(APIView):
    def get(self, request, format = None):
        itemCredentials = Item.objects.all()
        serializer = itemSerializer(itemCredentials, many =True)
        return Response(serializer.data)

# This is for endpoint 10

class submitItem(APIView):
    def post(self, request, format=None):
        serializer = itemSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This is for endpoint 15

class deletePurchaseRequest(APIView):
    def delete(self, request, pk, format=None):
        requests = PurchaseRequest.objects.filter (pk=pk)
        requests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)