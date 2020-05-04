from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    username = None
    ID = models.CharField("User's ID", max_length=200, unique=True)
    substation = models.CharField("Substation location", max_length=200, unique=True)  
    USERNAME_FIELD = 'ID'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
        
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

