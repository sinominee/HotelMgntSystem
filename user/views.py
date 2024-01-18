from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 

# function view ko use gare ko bhayee rah yo use garneh so that we are able to enteract in swagger
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    # request.query_params.get('int')   '''this is used for query param http://127.0.0.1:8000/login/?int=1'''

    user = authenticate(username=email, password=password)

    if  user != None:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    else:
        return Response('Invalid credentials!')
    