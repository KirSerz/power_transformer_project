from django.contrib import admin
from .models import User, Substation, Transformer, DataDGA

# Register your models here.

admin.site.register(User)
admin.site.register(Substation)
admin.site.register(Transformer)
admin.site.register(DataDGA)