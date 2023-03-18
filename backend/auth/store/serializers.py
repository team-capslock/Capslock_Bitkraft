from rest_framework import serializers
from .models import *

class StoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreDetail
        fields = '__all__'

