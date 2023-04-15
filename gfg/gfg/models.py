from django.db import models

# creating the required models 

class Entrepreneur(models.Model):
    name:models.CharField(max_length=200)
    email:models.CharField(max_length=100)
    patent:models.TextField()
    phone:models.IntegerField()