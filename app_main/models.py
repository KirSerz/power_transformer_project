from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class Substation(models.Model):
    name = models.CharField("Название организации", max_length=200, default='')
    city = models.CharField("Город", max_length=200, default='')
    street = models.CharField("Улица", max_length=200, default='')
    descriptions = models.CharField("Описание", max_length=200, default='')
    date = models.DateTimeField('Дата изменениея баланса', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
	    verbose_name_plural = "Подстанция"

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

