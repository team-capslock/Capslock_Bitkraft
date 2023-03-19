from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from django.http import JsonResponse
# Create your views here.
from rest_framework import status
import requests
from django.views.decorators.csrf import csrf_exempt
import secrets
@api_view(['POST'])
def add_product(request):
    try:
        store_id = request.query_params.get('store_id')
        print("request.data:",request.data)
        for i in request.data:    
            data = i 
            i['store'] = store_id
            serializers_data = ProductSerializer(data=i,many=True)
            if serializers_data.is_valid():
                serializers_data.save()
                return JsonResponse({"data":serializers_data.data},status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error":serializers_data.errors})
    except Exception as e:
        # message = serializers.errors 
        print("error",e)
        return JsonResponse({"message":"dd"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_product(request):
    queryset = ProductDetail.objects.all()
    serialized_data = ProductSerializer(queryset,many=True)
    print(serialized_data)
    return JsonResponse({"serialized_data":serialized_data.data})


# def getUserInfo(request):
# @api_view(['GET'])
def get_location(request,ip):
    # ip_address = get_ip()
    ip = '103.220.42.201'
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()
    print("response:",response)
    location_data = {
        "ip": ip,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    # return JsonResponse({"location_data":location_data})
    return location_data

@api_view(['POST'])
@csrf_exempt
def add_hit(request):
    try:
        data = request.data
        product_name = data.get('product_name')
        store_url = data.get('store_url')
        product = ProductDetail.objects.get(name=product_name,store__url=store_url)
        print("product:",product)   
        if not product:
            data['store'] = product.store
            # data['product'] = product_id
            ip = data.get('ip')
            location_data = get_location(request,ip)
            data['city'] = location_data['city']
            data['state'] = location_data['state']
            data['country'] = location_data['country']
            serializer = HitSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg":"New Hit Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            data = ProductSerializer(product).data
            return JsonResponse({"data":data},status=status.HTTP_200_OK)
    except Exception as e:
        print("error",e)
        return JsonResponse({"message":"dd"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def get_user_level(request):
    try:
        api_key = ""
        web_url = request.data.get('url')
        queryset = StoreDetail.objects.filter(url=web_url)
        if len(queryset)>0:
            
            product_queryset = ProductDetail.objects.filter(store__url=web_url)
            if product_queryset:
                api_key = product_queryset.last().store.api_key
                print(api_key)
                return JsonResponse({"val":2,"api_key":api_key},status=status.HTTP_200_OK)
            else:
                return JsonResponse({"val":1,"api_key":api_key},status=status.HTTP_200_OK)
        else:
            return JsonResponse({"val":0})

    except Exception as e:
        print("error:",e)
        return JsonResponse({"msg":"Error"},status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
def create_api_key(request):
    secret_key = secrets.token_hex(16)
    return secret_key

