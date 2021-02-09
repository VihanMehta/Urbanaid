from django.db import models
from django.core.validators import MinLengthValidator

class contactus(models.Model):
    Name = models.CharField(max_length=25, null=False)
    email = models.CharField(max_length=50, null=False)
    Message = models.TextField(null=False)

    def __str__(self):
        return self.email
    

class User_mst(models.Model):
    UserName = models.CharField(max_length=15, null=False, unique=True)
    Password = models.CharField(max_length=500, null=False)
    FirstName = models.CharField(max_length=10, null=False)
    LastName = models.CharField(max_length=10, null=False)
    Gender = models.CharField(max_length=1, null=False)
    Email = models.CharField(max_length=35, null=False, unique=True)
    ContactNo = models.CharField(max_length=10, null=False, unique=True)

    def register(self):
        self.save()

    def __str__(self):
        return self.UserName

    @staticmethod
    def get_User_mst_by_Email(UserName):
        try:
            return User_mst.objects.get(UserName=UserName)
        except:
            return False

    def EmailisExists(self):
        if User_mst.objects.filter(Email = self.Email):
            return True
        return  False
    
    def Emailcheck(newemail):
        if User_mst.objects.filter(Email = newemail):
            return True
        return  False

    def UserisExists(self):
        if User_mst.objects.filter(UserName = self.UserName):
            return True
        return  False

    def PhoneisExists(self):
        if User_mst.objects.filter( ContactNo = self.ContactNo):
            return True
        return  False