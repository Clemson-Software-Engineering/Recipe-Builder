from django.urls import path
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    path('account/login', TemplateView.as_view(template_name = 'Recipe-Builder_Home.html')),
    path('product', views.product),
    path('recipe', views.recipe),
    path('addToList', views.addToList),
    path('delete/<str:name>/', views.delete),
]
