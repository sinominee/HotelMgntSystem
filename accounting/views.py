from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Bill,Payment
from rest_framework.response import Response
from .serializers import BillSerializer
from rest_framework.viewsets import ModelViewSet
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

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
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