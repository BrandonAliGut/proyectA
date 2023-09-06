from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import Base64ImageField

class SerializerCategoria(serializers.ModelSerializer):
    img = Base64ImageField(required= False)
    class Meta:
        model = Category
        fields = ['id','name','img', 'information','update_at','created_at']