from django.contrib import admin
from .models import Category, RecipieIngredient, Ingredient, Recipie

# Register your models here.
admin.site.register(Category)
admin.site.register(RecipieIngredient)
admin.site.register(Ingredient)
admin.site.register(Recipie)


