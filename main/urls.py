
from main.views import all_product
from django.urls import path,include
from django.contrib import admin
urlpatterns = [
    path('', all_product)
]
