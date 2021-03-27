from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.TextField()
    price = models.FloatField()

class Recipe(models.Model):
    name = models.TextField(default="")
    ingredients = models.ManyToManyField('Ingredient')

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField('Recipe')
