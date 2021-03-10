from rest_framework import serializers
from .models import InvoiceModel

class InvoiceSerializer (serializers.ModelSerializer):
    class Meta:
        model = InvoiceModel
        fields = ['id', 'company_name']

class InvoiceSerializerAll (serializers.ModelSerializer):
    class Meta:
        model = InvoiceModel
        fields = ['id', 'company_name', 'file_location', 'invoice_info']