from django.db import models

# Create your models here.

class Insta_profiles(models.Model):
    name = models.CharField(max_length = 100)
    follower_count = models.IntegerField()
    following_count = models.IntegerField()
    genere = models.CharField(max_length=200)
    bio = models.CharField(max_length = 1000)
    city = models.CharField(max_length = 100)
    contact_details = models.CharField(max_length = 200)
    
