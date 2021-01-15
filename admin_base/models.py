from django.db import models
from prof_base.models import Professional_mst
from django.urls import reverse

class Professional_mst(models.Model):
    UserName = models.CharField(max_length=10, null=False, unique=True)
    Password = models.CharField(max_length=15, null=False)
    FirstName = models.CharField(max_length=10, null=False)
    LastName = models.CharField(max_length=10, null=False)
    Gender = models.CharField(max_length=1, null=False)
    Email = models.CharField(max_length=30, null=False, unique=True)
    ContactNo = models.CharField(max_length=10, null=False, unique=True)
    Qualification = models.CharField(max_length=50, null=False)

    def __str__(self):
        return (self.UserName)
    
class Category_mst(models.Model):
    CategoryName = models.CharField(max_length=25, db_index=True ,null=False)
    slug= models.SlugField(max_length=200,unique=True)
    
    def __str__(self):
        return self.CategoryName

class Service_mst(models.Model):
    Categoryid = models.ForeignKey('Category_mst', max_length=7, on_delete=models.CASCADE)
    Professionalid = models.ForeignKey('Professional_mst', max_length=5, on_delete=models.CASCADE)
    ServiceName=models.CharField(max_length=20, db_index=True)
    slug= models.SlugField(max_length=200,unique=True)
    image=models.ImageField(upload_to='services/%Y/%m/%d', blank = True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ServiceName

# Create your models here.
