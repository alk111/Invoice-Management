from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.user.username

class Plan(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)
    billing_period = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    pricing_model = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username

class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)
    billing_cycle = models.CharField(max_length=30)
    auto_collection = models.CharField(max_length=30)
    

    def __str__(self):
        return self.user.username