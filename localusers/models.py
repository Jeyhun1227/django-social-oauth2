
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class LocalUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(_("email_address"), max_length=254)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.PhoneNumberField(_("phone_number"))
    
