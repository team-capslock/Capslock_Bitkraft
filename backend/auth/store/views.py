from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from product.views import create_api_key
# Create your views here.

def create_store(request,user):
    api_key = create_api_key(request)
    data = request.data['store_data'] 
    data['user'] = user.id
    data['api_key'] = api_key
    serializers = StoreDetailSerializer(data=data)
    print("On 10",serializers)
    if serializers.is_valid():
        serializers.save()
        return serializers.data 

        # return data


    