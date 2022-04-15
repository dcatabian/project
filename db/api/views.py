from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import invoiceSerializer, itemSerializer, loginSerializer, prSerializer, memberSerializer
from .models import Invoice, LoginInfo, Member, PurchaseRequest, Item
#from db.api import serializers

# Create your views here.

# Endpoint 1
class getLogin(APIView):
    def try_getting(self, uname):
        try:
            return LoginInfo.objects.filter(username = uname)
        except PurchaseRequest.DoesNotExist:
            raise Http404

    def get(self, request, uname, format=None):
        credentials = self.try_getting(uname)
        serializer = loginSerializer(credentials, many = True)
        return Response(serializer.data)

# Endpoint 2 and endpoint 8
class allpurchaseRequest(APIView):
    def get(self, request, format = None):
        purchaseCredentials = PurchaseRequest.objects.all()
        serializer = prSerializer(purchaseCredentials, many =True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = prSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """
        try:
            posted = Member.objects.get(pk=request.sub)
            niname = request.iname
            nquant = request.quant
            ncost = request.cost
            narg = request.arg
            newPR = PurchaseRequest(sub_id = posted, app_id = None, 
                iname = niname,
                quant = nquant,
                cost = ncost,
                arg = narg)
            if newPR.is_valid():
                newPR.save()
                return Response(newPR.data, status=status.HTTP_201_CREATED)
            return Response (newPR.errors, status=status.HTTP_400_BAD_REQUEST)
        except Member.DoesNotExist:
            raise Http404"""

# endpoint 3

class userPurchaseRequest(APIView):
    def get(self, request, u, format = None):
        #user = Member.objects.get(pk=u)
        theirs = PurchaseRequest.objects.filter(sub_id__pk=u)
        serializer = prSerializer(theirs, many = True)
        return Response(serializer.data)

# endpoints 4, 12, 15

class idPurchaseRequest(APIView):
    def try_getting(self, pk):
        try:
            return PurchaseRequest.objects.get(pk=pk)
        except PurchaseRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        specific = self.try_getting(pk)
        serializer = prSerializer(specific)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        toMod = self.try_getting(pk)
        serializer = prSerializer(toMod, data = request.data)
        if serializer.is_valid():    
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        requests = self.try_getting(pk)
        requests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

# endpoint 13
class updateInvoice(APIView):
    def try_getting(self, pk):
        try:
            return Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        specific = self.try_getting(pk)
        serializer = invoiceSerializer(specific)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        toMod = self.try_getting(pk)
        serializer = invoiceSerializer(toMod, data = request.data)
        if serializer.is_valid():    
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# endpoint 14
class updateItem(APIView):
    def try_getting(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        specific = self.try_getting(pk)
        serializer = itemSerializer(specific)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        toMod = self.try_getting(pk)
        serializer = itemSerializer(toMod, data = request.data)
        if serializer.is_valid():    
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# endpoints 6, 10
class allItems(APIView):
    def get(self, request, format = None):
        itemCredentials = Item.objects.all()
        serializer = itemSerializer(itemCredentials, many =True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = itemSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
