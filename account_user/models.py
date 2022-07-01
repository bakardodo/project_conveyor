from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class ConveyorUser(AbstractBaseUser, PermissionsMixin):
