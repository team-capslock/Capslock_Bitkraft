from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import random
from .models import OTP

def email_otp(user):
    try:
        otp = random.randint(1000,9999)
        subject = f"Your One Time Password."
        msg = f"OTP :: {otp}"
        html_message = render_to_string('main/otp_email.html', {"otp": otp})
        response = send_mail(subject, msg, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message, fail_silently=False)
        if response == 1:
            OTP.objects.create(user=user,otp=otp)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False