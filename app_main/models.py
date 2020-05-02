from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

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

class Transformer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transformer_ID = models.CharField("Transformer's ID", max_length=200, unique=True)
    location = models.CharField("Location", max_length=200, unique=True)

class DataDGA(models.Model):
    
    transformer = models.ForeignKey(Transformer, on_delete=models.CASCADE)
    data_dga = models.TextField('Данные DGA(json)', blank=True, default='')
    classification_score = models.FloatField('Оценка классификатора', default=0)   
    
    