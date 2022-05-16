from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class messageModelViewSet(viewsets.ModelViewSet):
    queryset = message.objects.all()
    serializer_class = messageSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]



#Custom token
#custom auth token for additional info/data
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#endpoint with using customauthentication to add additional details are as : email and id etc.
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
