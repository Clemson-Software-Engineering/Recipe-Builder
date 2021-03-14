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
def product(request):
    service_client = KrogerServiceClient(encoded_client_token=encoded_client_token)
    products = service_client.search_products(term="Taco", limit=10, location_id='02600845')
    return render(request, 'Recipe-Builder_Home.htm')

# @login_required(redirect_field_name='itemlist')
def form(request):
    # user_settings, created = UserSettings.objects.get_or_create(user = request.user)
    # , context = {"items": user_settings.items.all() } goes after request etc.
    return render(request, 'Recipe-Builder_Form.htm')

def addToList(request):
    # price = requests.get(url).json()['latestPrice']
    # item, created = Ingredient.objects.get_or_create(name = name, price=price)
    # item.save()
    # current_user = request.user #get current users info
    # user_settings, created = UserSettings.objects.get_or_create(user = current_user)
    # user_settings.recipe.add(item)
    # user_settings.save()

    return render(request, 'Recipe-Builder_Results.htm')

def delete(request, ingredient):
    ing = Ingredient.objects.get(name = name, price=price)

    current_user = request.user
    user_settings = UserSettings.objects.get(user = current_user)

    # import pdb; pdb.set_trace()
    user_settings.ing.remove(name)
    user_settings.save()

    return redirect('itemlist')
def recipe(request):
    return render(request, 'Recipe-Builder_Results.htm')
