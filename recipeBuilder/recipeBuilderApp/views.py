from django.shortcuts import render
import requests, time
from recipeBuilderApp.models import Ingredient, UserSettings, Recipe
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template import Context, Template
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
@login_required(redirect_field_name='home')
def submit_form(request):
    if(request.method=='POST' and 'save' in request.POST):
        service_client = KrogerServiceClient(encoded_client_token=encoded_client_token)
        recipe = request.POST.get('recipeName')
        recipe, created = Recipe.objects.get_or_create(name=recipe)
        ingredients = request.POST.getlist('ingredient')
        for item in ingredients:
            if not item:
                break
            product = str(service_client.search_products(term=item, limit=1, location_id='02600845'))
            tuple = product.split(":")
            tempIngredient, created = Ingredient.objects.get_or_create(name=tuple[0], price=tuple[1])
            tempIngredient.save()
            recipe.ingredients.add(tempIngredient)
        recipe.save()
        user_settings, created = UserSettings.objects.get_or_create(user = request.user)
        user_settings.recipes.add(recipe)
        user_settings.save()

        context = {}
        recipeList = user_settings.recipes.all()
        for userRecipe in recipeList:
            context[userRecipe.name] = [item.name for item in userRecipe.ingredients.all()]
        return render(request, 'Saved_Recipes.htm', context)


    elif(request.method=='POST' and 'results' in request.POST):
        service_client = KrogerServiceClient(encoded_client_token=encoded_client_token)
        recipe, created = Recipe.objects.get_or_create(name="")
        recipe.delete()
        recipe, created = Recipe.objects.get_or_create(name="")
        ingredients = request.POST.getlist('ingredient')
        for item in ingredients:
            if not item:
                break
            product = str(service_client.search_products(term=item, limit=1, location_id='02600845'))
            tuple = product.split(":")
            result, created = Ingredient.objects.get_or_create(name=tuple[0], price=tuple[1])
            result.save()
            recipe.ingredients.add(result)
        recipe.save()
        return render(request, 'Recipe-Builder_Results.htm', context={"recipe": recipe.ingredients.all()})

def showRecipes(request):
    user_settings, created = UserSettings.objects.get_or_create(user = request.user)
    print(user_settings.recipes.all())
    return render(request, 'Saved_recipes.htm', context={"recipes": user_settings.recipes.all()})

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
