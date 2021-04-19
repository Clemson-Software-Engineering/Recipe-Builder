# forms.py
from django.forms import modelformset_factory
from .models import Ingredient, Recipe, UserSettings

# A regular form, not a formset
RecipeFormSet = modelformset_factory(
    Recipe, fields=("name", "ingredients"), extra= 1
)
