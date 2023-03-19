from django.urls import path
from . import views
from product.views import *
from store.views import *
app_name = 'main'
urlpatterns = [
    path('api/register', views.register, name='register'),
    path('api/signin', views.signin, name='signin'),
    path('api/send-otp', views.send_otp, name='send_otp'),
    path('api/verify-otp', views.verify_otp, name='verify_otp'),
    path('api/dashboard', views.dashboard, name='dashboard'),
    path('api/add-product',add_product),
    path('api/get-product',get_product),  
    path('api/get-location',get_location),  
    path('api/add-hit',add_hit),  
    path('api/get-user-level',get_user_level),  
    path('api/get-store-product',get_store_product),
]