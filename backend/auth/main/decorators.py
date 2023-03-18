from functools import wraps
from django.http import HttpResponseBadRequest
from rest_framework import serializers,status
from rest_framework.response import Response


def serializer_validator(serializer_class):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            try:
                data = request.data
                serializer = serializer_class(data=data)
                serializer.is_valid(raise_exception=True)
            except (ValueError, serializers.ValidationError):
                message = list(serializer.errors.values())[0]
                return Response({"error": message},status=status.HTTP_400_BAD_REQUEST)
            kwargs['serializer_data'] = serializer.validated_data['user']
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

def verified_user(serializer_class):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            try:
                data = request.data
                serializer = serializer_class(data=data)
                serializer.is_valid(raise_exception=True)
            except (ValueError, serializers.ValidationError):
                message = list(serializer.errors.values())[0]
                return Response({"error": message},status=status.HTTP_400_BAD_REQUEST)
            kwargs['serializer_data'] = serializer.validated_data['user']
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
