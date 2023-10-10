from django.db import models
from django.contrib.auth.models import User


class patient (models.Model):
    patientID = models.CharField(max_length = 16)
    name = models.CharField(max_length = 60)
    phone = models.CharField(max_length = 20)
    bloodgroup = models.CharField(max_length = 20)
    checkup = models.BooleanField()

class appointment(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    doctor=models.CharField(max_length=40)
    phone = models.CharField(max_length = 20)
    date=models.CharField(max_length = 20)
    time=models.CharField(max_length = 20,unique="True")
    symtoms=models.CharField(max_length = 50)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone = models.CharField(max_length = 20)
    gender=models.CharField(max_length = 20)
    comments=models.CharField(max_length = 60)

    def __str__(self):
        return self.name
