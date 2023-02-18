from django_tables2 import tables, TemplateColumn
from .models import Ingredient, RecipieIngredient, Recipie, Category
from django.forms import ModelForm

class IngredientTable(tables.Table):
    class Meta:
        model = Ingredient
        row_attrs = {
            "ingredient_name": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead': {'class': 'thead-dark' }}
        fields = {'ingredient_name'}
    #edit = TemplateColumn(template_name='main/upd_create.html')
    #delete = TemplateColumn(template_name='main/delete.html')


class CategoryTable(tables.Table):
    class Meta:
        model = Category
        row_attrs = {
            "category_name": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark' }}
        fields = {'category_name'}
    #edit = TemplateColumn(template_name='main/upd_create.html')
    #delete = TemplateColumn(template_name='main/delete.html')



class RecipieTable(tables.Table):
    class Meta:
        model = Recipie
        row_attrs = {
            "recipie_name": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark'}}
        fields = {'recipie_name', 'category_name', 'description'}
    edit = TemplateColumn(template_name='main/update.html')
    #delete = TemplateColumn(template_name='main/delete.html')

class RecipieIngredientTable(tables.Table):
    class Meta:
        model = RecipieIngredient
        row_attrs = {
            "recipie_ingredient_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped thead-dark",
                  'thead' : {'class': 'thead-dark'}}
        fields = {'recipie_ingredient_id', 'recipie_name','ingredient', 'unit_of_measure', 'value'}
    #edit = TemplateColumn(template_name='main/upd_create.html')
    #delete = TemplateColumn(template_name='main/delete_column_recipie_ingredient.html')

1