from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.TextField()
    price = models.FloatField()

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recipes = models.OneToMany(Recipe)

class Recipe(models.Model):
    name = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)
