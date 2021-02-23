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
    
    @staticmethod
    def get_prof_mst_by_username(UserName):
        try:
            return Professional_mst.objects.get(UserName=UserName)
        except:
            return False

class Professional_Contact(models.Model):
     FirstName = models.CharField(max_length=10, null=False)
     LastName = models.CharField(max_length=10, null=False)
     ContactNo = models.CharField(max_length=10, null=False, unique=True)

# Create your models here.