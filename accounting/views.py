from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Bill,Payment
from rest_framework.response import Response
from .serializers import BillSerializer
from rest_framework.viewsets import ModelViewSet
from core.permissions import CustomPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

#ModelViewset chai class base ko lagi 
# Create your views here.

# function based view: use gare ko ho
# @api_view(['GET'])
# def bill_view(request):
#     bill_obj = Bill.objects.all()
#     bill_json = BillSerializer(bill_obj,many=True)
#     return Response(bill_json.data)

# Class based view:
class BillView(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [CustomPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['guest']
    Search_fieldsr = ['amount', ]

    def list(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset,many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        try:
            queryset = Bill.objects.get(id=pk)
        except:
            return Response({"error":"Not Found!"})    
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        try:
            queryset = Bill.objects.get(id=pk)
        except:
            return Response({"error":"Not Found!"})    
        serializer = self.serializer_class(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def destroy(self, request, pk=None):
        try: 
            queryset = Bill.objects.get(id=pk)
        except:
            return Response({"error":"Not Found!"})    
        queryset.delete()
        return Response('data deleted!')