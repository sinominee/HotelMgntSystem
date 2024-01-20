from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import EmployeeInfo
from .serializers import EmployeeInfoSerializer
from user.serializers import UserSerializer
from rest_framework.response import Response
from user.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework.filters import SearchFilter

# Create your views here.
class EmployeeInfoView(ModelViewSet):
    queryset = EmployeeInfo.objects.all()
    serializer_class = EmployeeInfoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'number']

    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        group_id = request.data.get('group')
        group_obj = Group.objects.get(id=group_id)
        hash_password = make_password(password)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = User.objects.create(email=email,password=hash_password)
                user.groups.add(group_obj)
                a = serializer.save()
                a.user = user
                a.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response(serializer.errors)