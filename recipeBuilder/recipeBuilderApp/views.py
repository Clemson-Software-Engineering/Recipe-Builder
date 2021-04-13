from django.shortcuts import render
import requests, time
from recipeBuilderApp.models import Ingredient, UserSettings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .python_kroger_client.client import (
    KrogerCustomerClient,
    KrogerServiceClient,
)
from .python_kroger_client.config import (
    customer_username,
    customer_password,
    encoded_client_token,
    redirect_uri,
)
# def product(request):
#     service_client = KrogerServiceClient(encoded_client_token=encoded_client_token)
#     products = service_client.search_products(term="Taco", limit=1, location_id='02600845')
#     return render(request, 'Recipe-Builder_Home.htm')

# @login_required(redirect_field_name='itemlist')

#super user: recipebuilder, recipebuilder
#sample user: recipebuilder, Cuser!Clemson
def form(request):
    return render(request, 'Recipe-Builder_Form.htm')

# @login_required
def addRecipe(request):
    user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    service_client = KrogerServiceClient(encoded_client_token=encoded_client_token)
    recipe, created = Recipe.objects.get_or_create(name=request.name)
    while(True):
        item_name = request.POST['ingredient']
        ingredient = Ingredient.objects.get_or_create(name=item_name)
        recipe.ingredients.add(ingredient)
    recipe.save()

def showRecipe(request):
    return render(request, 'Saved_recipes.htm', context={"recipes": user_settings.reipces.all()})

def addToList(request):
    user_settings, created = UserSettings.objects.get_or_create(user = request.user)
    service_client = KrogerServiceClient(encoded_client_token=encoded_client_token)
    return render(request, 'Recipe-Builder_Results.php', context = {"ingredients": user_settings.ingredients.all()})

def about(request):
    return render(request, 'Recipe-Builder_About.htm')

def delete(request, ingredient):
    ing = Ingredient.objects.get(name = name, price=price)

    current_user = request.user
    user_settings = UserSettings.objects.get(user = current_user)

    # import pdb; pdb.set_trace()
    user_settings.ing.remove(name)
    user_settings.save()

    return redirect('itemlist')

def results(request):
    return render(request, 'Recipe-Builder_Results.php')
