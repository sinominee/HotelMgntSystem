from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 
# function view ko use gare ko bhayee rah yo use garneh so that we are able to enteract in swagger
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer,GroupSerializer
from rest_framework.permissions import AllowAny,IsAdminUser
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group



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

# onwer ko lagi      
@api_view(['POST'])
@permission_classes([IsAdminUser])
def owner_create(request):
    email = request.data.get('email')
    password = request.data.get('password')
    group = Group.objects.get(name='Owner')
    ''' done so user ko id is valid or not unique or not '''
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        hash_password = make_password(password)
        a = User.objects.create(email=email,password=hash_password)
        a.groups.add(group)
        return Response('User created successfully!')
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def group_list(request):
    group_objs = Group.objects.all().exclude(name='Owner')
    serializer = GroupSerializer(group_objs,many=True)
    return Response(serializer.data)

