from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('api/register', views.register, name='register'),
    path('api/signin', views.signin, name='signin'),
    path('api/send-otp', views.send_otp, name='send_otp'),
    path('api/verify-otp', views.verify_otp, name='verify_otp'),
    path('api/dashboard', views.dashboard, name='dashboard'),
    
]