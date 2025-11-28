from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password,check_password


class RegisterSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','password']
        
    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)


