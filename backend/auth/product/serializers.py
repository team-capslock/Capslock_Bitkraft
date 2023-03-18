from rest_framework import serializers
from .models import *
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'

class HitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hit
        fields = '__all__'