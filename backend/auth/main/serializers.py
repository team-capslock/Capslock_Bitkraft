from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'mobile')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name', 'mobile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'], 
            password = validated_data['password'], 
            name = validated_data['name'], 
            mobile = validated_data['mobile']
            )
        
        return user
    
# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        username = data.get('email')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = _('Invalid email or password.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data

# Requested User Serializer
class RequestedUserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    
    def validate(self, data):
        user_id = data.get('id')
        email = data.get('email')

        if user_id and email:
            try:
                user = User.objects.get(id=user_id, email=email)
            except:
                user = None
            if not user:
                msg = _('User not found')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include user id and email')
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data

class RequestedUserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    
    def validate(self, data):
        user_id = data.get('id')
        email = data.get('email')

        if user_id and email:
            try:
                user = User.objects.get(id=user_id, email=email)
            except:
                user = None
            if not user:
                msg = _('User not found')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include user id and email')
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data
    
    
class VerfiedUserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    
    def validate(self, data):
        user_id = data.get('id')
        email = data.get('email')

        if user_id and email:
            try:
                user = User.objects.get(id=user_id, email=email)
                print("user:",user)
            except:
                user = None
            if not user:
                print("In if")
                msg = _('User not found.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include user id and email')
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data