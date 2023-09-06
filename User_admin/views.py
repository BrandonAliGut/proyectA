from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .models import User_models

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import *
from .permissions import UpdateOwnProfile
from django.contrib.auth import authenticate, login
# Create your views here.

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login


from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class UserViewset(viewsets.ModelViewSet):
    serializer_class = User_serializar
    queryset = User_models.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('last_name','email','name')
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        user = serializer.validated_data['user']
        password=serializer.validated_data['password']
        
        

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    


class UserLoginApiView(ObtainAuthToken):
    
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        password=serializer.validated_data['password']
        
        
        usermodel = User_models.objects.get(pk = user.pk)

        token, created = Token.objects.get_or_create(user=usermodel)
        user_autheticated = authenticate(request,username=user, password=password)
        if user is not None:
            login(request, user_autheticated)
        
        return Response({
            'user':  {
                'id': user.pk,
                'email':user.email,
                'name': user.name,
                'last_name':user.last_name,
                },
            'token': token.key
            })
    
      
    
    





class ExampleView(APIView):
    
    #SessionAuthentication : permite el pase si existe una cession activa : authentication_classes = [.. , SessionAuthentication]
    
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):

        #print(request.user.get_group_permissions())
        if 'Api_Reciclaje_I.view_category' in request.user.get_group_permissions():
            if request.user.is_authenticated:
                content = {
                    'user': str(request.user),  # `django.contrib.auth.User` instance.
                    'auth': str(request.user.is_authenticated),  # None
                }
                return Response(content)
        
        return Response(data = { "detail": "not esta autorizado"}, status=400)
            