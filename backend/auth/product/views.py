from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import *
from django.http import JsonResponse
# Create your views here.
from rest_framework import status
import requests
from django.views.decorators.csrf import csrf_exempt
import secrets
import json

@api_view(['POST'])
def add_product(request):
    try:
        store_url = request.data.get('store_url')
        print("request.data:",request.data)
        prod_list = json.loads(request.data.get('products'))
        for i in prod_list:
            try:
                prod = ProductDetail.objects.get(name=i[0],store__url=store_url)
            except:
                prod = None
            if not prod:
                ProductDetail.objects.create(store=StoreDetail.objects.get(url=store_url),name=i[0],description=i[1],price=i[0],image_url=i[2]);
        return JsonResponse({"message":"successful"},status=status.HTTP_200_OK)
            
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
import requests
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location(request,ip):
    ip = get_ip();
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()
    print("response:",response)
    location_data = {
        "ip": response.get("ip"),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "postal": response.get("postal")
    }
    # return JsonResponse({"location_data":location_data})
    return location_data

@api_view(['POST'])
@csrf_exempt
def add_hit(request):
    try:
        data = request.data
        print(data)
        product_name = data.get('product_name')
        store_url = data.get('store_url')
        try:
            print("store_url:",store_url)
            product = ProductDetail.objects.filter(name=product_name,store__url=store_url)
            print("product",product)
        except Exception as e:
            print(e)
            product = None
        print("product:",product.last())   
        if product:
            data['store'] = product.last().store.id
            # data['product'] = product_id
            ip = data.get('ip')
            location_data = get_location(request,ip)
            data['ip'] = location_data['ip']
            data['city'] = location_data['city']
            data['state'] = location_data['region']
            data['country'] = location_data['country']
            data['postal'] = location_data['postal']
            serializer = HitSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg":"New Hit Added Successfully"},status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return JsonResponse({"message":"dd"},status=status.HTTP_400_BAD_REQUEST)
            # data = ProductSerializer(product).data
            return JsonResponse({"data":data},status=status.HTTP_200_OK)
    except Exception as e:
        print("error",e)
        return JsonResponse({"message":"dd"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def get_user_level(request):
    try:
        api_key = ""
        web_url = request.data.get('url')
        l = len(web_url)
        
        web_url_sliced = web_url[:l-1]
        
        print("String : ",web_url_sliced)
        print(web_url)
        queryset = StoreDetail.objects.get(url=web_url_sliced)
        if queryset:
            product_queryset = ProductDetail.objects.filter(store__url=web_url_sliced)
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

