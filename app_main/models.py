from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class Substation(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
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
    """добавить спецификации трансформатора"""

    date_add = models.DateTimeField(auto_now_add=True)
    substation = models.ForeignKey(Substation, on_delete=models.CASCADE)
    unique_key = models.CharField("Transformer's ID", max_length=200, default='')
    descriptions = models.TextField("Описание", max_length=200, default='')

    def __str__(self):
        return '{0} {1}'.format(self.unique_key, self.substation)
    
    def upload_data(
        self, 
        classification_score=None, 
        data_dga=None
    ):
        new_item = DataDGA()
        new_item.transformer = self
        new_item.data_dga = data_dga
        new_item.classification_score = classification_score
        new_item.save()

    class Meta:
	    verbose_name_plural = "Трансформатор"

class DataDGA(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    transformer = models.ForeignKey(Transformer, on_delete=models.CASCADE)
    data_dga = models.TextField('Данные DGA(json)', blank=True, default='')
    classification_score = models.FloatField('Оценка классификатора', blank=True, null=True, default=None)
    
    def __str__(self):
        return '{0}'.format(self.classification_score)
    
    class Meta:
	    verbose_name_plural = "Данные DGA"
