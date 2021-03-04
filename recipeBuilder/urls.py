from django.urls import path

from . import views

urlpatters = [
    path('product', views.product),
    path('recipe', views.recipe),
    path('addToList', views.addToList),
    path('delete/<str:name>/', views.delete),
]
