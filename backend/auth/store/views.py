from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from product.models import Hit
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

@api_view(['POST'])
def get_store_product(request):
    store_url = request.data['store_url']
    queryset = Hit.objects.filter(store__url=store_url).count().select_related('product')
    print(queryset)
    return JsonResponse({"serialized_data":""})

        # return data