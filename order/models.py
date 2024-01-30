from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)



class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    order_details = models.TextField()
    
    is_completed = models.BooleanField(default=False)