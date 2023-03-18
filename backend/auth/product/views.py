from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from django.http import JsonResponse
# Create your views here.
from rest_framework import status
@api_view(['POST'])
def add_product(request):
    try:
        store_id = request.query_params.get('store_id')
        for i in request.data:    
            data = request.data['product_data'] 
            data['store'] = store_id
            serializers = ProductSerializer(data=data)
            
            if serializers.is_valid():
                serializers.save()
                return JsonResponse({},status=status.HTTP_200_OK)
    except Exception as e:
        message = serializers.errors 
        return JsonResponse({"message":message},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_product(request):
    queryset = ProductDetail.objects.all()
    serialized_data = ProductSerializer(queryset,many=True)
    print(serialized_data)
    return JsonResponse({"serialized_data":serialized_data.data})
