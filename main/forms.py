from django.forms import ModelForm
from .models import Ingredient, RecipieIngredient, Recipie, Category

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecepieIngredientForm(ModelForm):
    class Meta:
        model = RecipieIngredient
        fields = '__all__'

class RecipieForm(ModelForm):
    class Meta:
        model = Recipie
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'