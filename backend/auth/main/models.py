from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Create your models here.
class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, email, username=None, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, username, password, **other_fields)
    
    def create_user(self, email, username=None, password=None, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        if password is not None:
            user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    # this fields are mandatory for all type of users
    username =  models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    
    USER_TYPE =  (
        ("0","ADMIN"),
        ("1","USER")
    )
    user_type = models.CharField(max_length=20, blank=True, choices=USER_TYPE, verbose_name=_("user_type"))

    # this fields for individual user
    name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)

    # details
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES, verbose_name=_("gender"))
    gender_on_profile = models.BooleanField(default=False)
    birthdate = models.DateField(blank=True, null=True)

    # user verfication
    is_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(blank=True, null=True)

    # mandatory
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    # settings
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = 'auth_user'
        

class OTP(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    otp = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        db_table = "OTP"