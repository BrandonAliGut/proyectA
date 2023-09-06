from rest_framework import serializers
from .models import User_models
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login


class User_serializar(serializers.ModelSerializer):
    class Meta: 
        model = User_models
        fields = ('id', "email",  "name","last_name", 'password')
        extra_kwargs = {
        
            'password':{
                'write_only':True,
                
                'style': {
                    'input_type':'password'
                }
            }
            }
    def create(self,validated_data):
        
        user = User_models.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            last_name = validated_data['last_name'],
            password = validated_data['password'],
            
        )
        
        group=Group.objects.get(name='user')
        group.user_set.add(user)
        
       
        
        return user
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop(password)
            instance.set_password(password)
            
        return super().update(instance, validated_data)