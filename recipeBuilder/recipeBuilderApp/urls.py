from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('home', TemplateView.as_view(template_name = 'Recipe-Builder_Home.htm')),
    path('recipes', views.showRecipes),
    path('submit_form', views.submit_form),
    path('aboutpage', views.about),
    path('form', views.form),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('delete/<str:name>/', views.delete),
    path('accounts/logout', TemplateView.as_view(template_name = 'home.html'))
]
