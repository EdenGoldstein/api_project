from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, generics 
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserLoginView(APIView):
        
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password) #Authenticate the user
        if user is not None:
            token, created = Token.objects.get_or_create(user=user) #create or retrieve a token for the user 
            return Response({'token':token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    