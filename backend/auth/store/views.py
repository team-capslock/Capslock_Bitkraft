from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
# Create your views here.

def create_store(request,user):
    data = request.data['store_data'] 
    data['user'] = user.id
    serializers = StoreDetailSerializer(data=data)
    print("On 10",serializers)
    if serializers.is_valid():
        serializers.save()
        return serializers.data 

        # return data

    