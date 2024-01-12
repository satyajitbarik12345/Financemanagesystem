from django.db import models

# Create your models here.
class Employees(models.Model):
    name =models.CharField(max_length=200)
    category =models.TextField()
    dateofexpense=models.DateField()
    amount=models.IntegerField()
    updatedat=models.TimeField()
    createdby=models.CharField(max_length=200)

