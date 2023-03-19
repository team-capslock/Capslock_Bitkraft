from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, RequestedUserSerializer, VerfiedUserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import login
from .utils import email_otp
from datetime import datetime
from .models import OTP
from .decorators import serializer_validator, verified_user
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from store.views import *

# Register API
@api_view(['POST'])
def register(request):
    print(request.data)
    serializer = RegisterSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
               
        store_data = create_store(request,user)
        print("store_data:",store_data)
        return Response({"user": UserSerializer(user).data,"store_data":store_data})
    except Exception as e:
        print("Errors : Register =  ",e)
        # message = list(serializer.errors.values())[0]
        message = serializer.errors
        return Response({"message": message},status=status.HTTP_400_BAD_REQUEST)
    
# Login API
@api_view(['POST'])
def signin(request):
    print(request.data)
    serializer = LoginSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({"user": UserSerializer(user).data})
    except Exception as e:
        print("Errors : Login =  ",e)
        message = list(serializer.errors.values())[0]
        return Response({"message": message},status=status.HTTP_400_BAD_REQUEST)
    
# Send OTP
@api_view(['POST'])
@serializer_validator(RequestedUserSerializer)
def send_otp(request,serializer_data):
    user = serializer_data
    email_response = email_otp(user)
    if email_response == 1:
        return Response({"message": "OTP sent!"})
    else:
        return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# Verify OTP
@api_view(['POST'])
@serializer_validator(RequestedUserSerializer)
def verify_otp(request,serializer_data):
    user = serializer_data
    try:
        otp = OTP.objects.filter(user_id=user.id,otp=request.data['otp']).latest('created_at')
    except Exception as e:
        otp = None
    if otp:
        user.is_verified = True
        user.email_verified_at = datetime.now()
        user.save()
        return Response({"message": "Verified Successfully"})
    else:
        return Response({"message": "Incorrect OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
@csrf_exempt 
@api_view(['POST'])
@verified_user(VerfiedUserSerializer)
def dashboard(request,serializer_data):
    return HttpResponseBadRequest('Logged in')