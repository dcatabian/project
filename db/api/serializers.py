from rest_framework import serializers
from . import models

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = '__all__'

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LoginInfo
        fields = ('member_id', 'username', 'password', 'memType')

class prSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseRequest
        fields = '__all__'

class invoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = '__all__'

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'