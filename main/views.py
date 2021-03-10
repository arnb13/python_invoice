from logging import exception
from django.shortcuts import render
from yaml import serialize

from .models import InvoiceModel
from .serializers import InvoiceSerializer, InvoiceSerializerAll

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from invoice2data import extract_data
from django.core.files.storage import FileSystemStorage


@api_view(['GET'])
def api_get_all(request):
    if request.method == 'GET':
        content = {}
        try:
            inv = InvoiceModel.objects.filter()
            serializer = InvoiceSerializer(inv, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        except:
            content = {'error': 'data not found'}
            return Response(content, status = status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def api_get_one(request, id):
    if request.method == 'GET':
        content = {}
        try:
            inv = InvoiceModel.objects.get(id = id)
            serializer = InvoiceSerializerAll(inv)
            return Response(serializer.data, status = status.HTTP_200_OK)

        except:
            content = {'error': 'data not found'}
            return Response(content, status = status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def api_invoice(request):
    if request.method == 'POST':
        try:
            file = request.FILES['pdf']
            fs = FileSystemStorage()
            filename, ext = str(file).split('.')
            f = fs.save(str(file), file)
            url = './' +  fs.url(f)
    
            result = extract_data(url)

            inv = InvoiceModel()
            inv.company_name = result['issuer']
            inv.file_location = url
            inv.invoice_info = result
            inv.save()

            serializer = InvoiceSerializerAll(inv)
            return Response (serializer.data, status = status.HTTP_200_OK)
        except:
            content = {'error': 'data not found'}
            return Response(content, status = status.HTTP_404_NOT_FOUND)
        
    
