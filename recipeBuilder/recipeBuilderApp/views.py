from django.shortcuts import render
import requests, time
from recipeBuilderApp.models import Ingredient, UserSettings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def product(request):
    baseURL = 'https://api.kroger.com/v1/'
    scope="product.compact"
    client_id="recipe-builder-1e7cdb57aa7cc7a53546b7b52754185b1131751567875226221"
    redirect_uri="http://localhost/recipebuilder"
    url = f'https://api.kroger.com/v1/connect/oauth2/authorize?scope={scope}}&client_id={client_id}}&redirect_uri={red_uri}&response_type=code'
    token = requests.get(url).json()['latestPrice']
    token =
    return render(request, 'stockpage.html', context = {"price": price, "symbols": symbols})

@login_required(redirect_field_name='itemlist')
def itemlist(request):
    user_settings, created = UserSettings.objects.get_or_create(user = request.user)
    return render(request, 'Recipe-Builder_Results.html', context = {"items": user_settings.items.all() })

def addToList(request):
    price = requests.get(url).json()['latestPrice']
    item, created = Ingredient.objects.get_or_create(name = name, price=price)
    item.save()
    current_user = request.user #get current users info
    user_settings, created = UserSettings.objects.get_or_create(user = current_user)
    user_settings.recipe.add(item)
    user_settings.save()

    return redirect('itemlist')

def delete(request, ingredient):
    ing = Ingredient.objects.get(name = name, price=price)

    current_user = request.user
    user_settings = UserSettings.objects.get(user = current_user)

    # import pdb; pdb.set_trace()
    user_settings.stocks.remove(name)
    user_settings.save()

    return redirect('itemlist')
