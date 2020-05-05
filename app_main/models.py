from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings
from django.db import models
from django.utils import timezone

class Substation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField("Название организации", max_length=200, default='')
    city = models.CharField("Город", max_length=200, default='')
    street = models.CharField("Улица", max_length=200, default='')
    descriptions = models.CharField("Описание", max_length=200, default='')

    def __str__(self):
        return self.name

    class Meta:
	    verbose_name_plural = "Подстанция"

class User(AbstractUser):
    username = None
    email = models.CharField("User's Email", max_length=200, unique=True)
    substation = models.ForeignKey(Substation, on_delete=models.CASCADE, blank=True, null=True, default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
        
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Transformer(models.Model):
    """добавить спецификации трансформатора"""

    date = models.DateTimeField(auto_now_add=True)
    substation = models.ForeignKey(Substation, on_delete=models.CASCADE)
    unique_key = models.CharField("Transformer's ID", max_length=200, default='')
    descriptions = models.TextField("Описание", max_length=200, default='')

    def __str__(self):
        return '{0} {1}'.format(self.unique_key, self.substation)
    
    class Meta:
	    verbose_name_plural = "Трансформатор"

class DataDGA(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    transformer = models.ForeignKey(Transformer, on_delete=models.CASCADE)
    data_dga = models.TextField('Данные DGA(json)', blank=True, default='')
    classification_score = models.FloatField('Оценка классификатора', blank=True, null=True, default=None)
    
    def __str__(self):
        return '{0}'.format(self.classification_score)
    
    class Meta:
	    verbose_name_plural = "Данные DGA"