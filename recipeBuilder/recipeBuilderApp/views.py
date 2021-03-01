from django.shortcuts import render
import requests, time
from recipeBuilderApp.models import Item, UserSettings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def product(request):
    token = ''
    product = request.GET.get('item_id', '')
    url = f'https://walmart.com/api/{symbols}/quote?token={token}' #this is just a sample URL
    price = requests.get(url).json()['latestPrice']
    return render(request, 'Recipe-Builder_Results.html', context = {"price": price, "symbols": symbols})

@login_required(redirect_field_name='itemlist')
def itemlist(request):
    user_settings, created = UserSettings.objects.get_or_create(user = request.user)
    return render(request, 'Recipe-Builder_Results.html', context = {"stocks": user_settings.stocks.all() })

def addToList(request):
    price = requests.get(url).json()['latestPrice']
    item, created = Item.objects.get_or_create(name = symbol.upper(), price=price)
    item.save()
    current_user = request.user #get current users info
    user_settings, created = UserSettings.objects.get_or_create(user = current_user)
    user_settings.recipe.add(item)
    user_settings.save()

    return redirect('itemlist')

def delete(request, itemid):
    item = Item.objects.get(name = itemid)

    current_user = request.user
    user_settings = UserSettings.objects.get(user = current_user)

    # import pdb; pdb.set_trace()
    user_settings.stocks.remove(stock.id)
    user_settings.save()

    return redirect('itemlist')


def home(request):
    
     return render(request, "recipeBuilderApp/Recipe-Builder_Home.html", context)
