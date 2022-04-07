from rest_framework import serializers
from . import models

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        Model = models.Member
        fields = '__all__'

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        Model = models.LoginInfo
        fields = ('member_id', 'username', 'password')

class prSerializer(serializers.ModelSerializer):
    class Meta:
        Model = models.PurchaseRequest
        fields = '__all__'

class invoiceSerializer(serializers.ModelSerializer):
    class Meta:
        Model = models.Invoice
        fields = '__all__'

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        Model = models.Item
        fields = '__all__'