from django.db import models

# Create your models here.
class signup(models.Model):
    name1=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    password=models.TextField(max_length=20)
    phone=models.BigIntegerField(max_length=10)