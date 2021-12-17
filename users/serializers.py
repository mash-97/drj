from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers


class UserRegisterSerializer(UserCreateSerializer):
    re_password = serializers.CharField(style={"input_type": "password"}, write_only=True, max_length=100)

    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
    
    def validate(self, attrs):
        re_password = attrs.get('re_password')
        password = attrs.get('password')
        if re_password != password:
            raise serializers.ValidationError({'re_password': "Passwords Don't Match"})
        
        attrs.pop('re_password')
        return super().validate(attrs)
    
    class Meta(UserCreateSerializer.Meta):
        fields = ['name', 'email', 'is_employee',  'password', 're_password']

