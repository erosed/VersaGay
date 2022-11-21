from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

class CustomUser(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField("Description", max_length=600, default='', blank=True)

    def __str__(self):
        return self.username

class Gasto(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    
    def __str__(self):
        return self.nombre
    
class calendario(models.Model):
    titulo = models.CharField(max_length=100)
    hecho = models.BooleanField(default= False)
    crear = models.DateTimeField(auto_now_add = True)
    fecha = models.DateTimeField(auto_now_add = False, auto_now = False, blank = True, null = True)

    def __str__(self):
        return self.titulo
