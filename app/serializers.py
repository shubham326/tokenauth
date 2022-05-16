from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        #fields = ['id', 'username', 'password', 'email']
        fields = ['id', 'username', 'password']
        
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class messageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = message
        fields = ['id', 'message', 'created_at', 'updated_at', 'created_by']
        #depth = 1
        
        
#note i don't use writeable nested serializer so have to use read only nested
# or u can keep it simple for making POST request