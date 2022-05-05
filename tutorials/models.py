from django.db import models

# Create your models here.

class typeUser(models.Model):
    description = models.CharField(max_length=50)

class statusUser(models.Model):
    description = models.CharField(max_length=50)


class User(models.Model):
    name = models.CharField(max_length=70, blank=False)
    username = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=100, blank=False)
    type = models.ForeignKey(to=typeUser, on_delete=models.PROTECT)
    status = models.ForeignKey(to=statusUser, on_delete=models.PROTECT)


