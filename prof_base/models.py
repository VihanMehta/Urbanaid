from django.db import models

class Professional_mst(models.Model):
    UserName = models.CharField(max_length=10, null=False, unique=True)
    Password = models.CharField(max_length=15, null=False)
    FirstName = models.CharField(max_length=10, null=False)
    LastName = models.CharField(max_length=10, null=False)
    Gender = models.CharField(max_length=1, null=False)
    Email = models.CharField(max_length=30, null=False, unique=True)
    ContactNo = models.CharField(max_length=10, null=False, unique=True)
    Qualification = models.CharField(max_length=50, null=False)
    address =models.CharField(max_length=500, null=True,blank=True)
    Postcode= models.CharField(max_length=10, null=True,blank=True)
    

class Professional_Contact(models.Model):
     FirstName = models.CharField(max_length=10, null=False)
     LastName = models.CharField(max_length=10, null=False)
     ContactNo = models.CharField(max_length=10, null=False, unique=True)

# Create your models here.