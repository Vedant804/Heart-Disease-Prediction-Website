from django.db import models


class User(models.Model):
    # Define your user model fields here
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    # Add more fields as needed



# Create your models here.
