from django.db import models

class User_mst(models.Model):
    UserName = models.CharField(max_length=15, null=False, unique=True)
    Password = models.CharField(max_length=25, null=False)
    FirstName = models.CharField(max_length=10, null=False)
    LastName = models.CharField(max_length=10, null=False)
    Gender = models.CharField(max_length=1, null=False)
    Email = models.CharField(max_length=35, null=False, unique=True)
    ContactNo = models.CharField(max_length=10, null=False, unique=True)

    def __str__(self):
        return self.UserName