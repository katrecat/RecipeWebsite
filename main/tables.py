from django_tables2 import tables, TemplateColumn
from .models import Ingredient, RecipieIngredient, Recipie, Category


class IngredientTable(tables.Table):
    class Meta:
        model = Ingredient
        row_attrs = {
            "ingredient_name": lambda record: record.pk
         }
        attrs = {'class': "table table-striped table-hover"}
        fields = {'ingredient_name'}


class CategoryTable(tables.Table):
    class Meta:
        model = Category
        row_attrs = {
            "category_name": lambda record: record.pk
         }
        attrs = {'class': "table table-striped table-hover"}
        fields = {'category_name'}


class RecipieTable(tables.Table):
    class Meta:
        model = Recipie
        row_attrs = {
            "recipie_name": lambda record: record.pk
         }
        attrs = {'class': "table table-striped table-hover"}
        fields = {'recipie_name', 'category_name', 'description'}
    T1 = '<a href={% url "update" record.pk %} class="btn btn-dark">update</a>'
    T2 = '<a href={% url "delete" record.pk %} class="btn btn-dark">delete</a>'
    edit = TemplateColumn(T1)
    delete = TemplateColumn(T2)


class RecipieIngredientTable(tables.Table):
    class Meta:
        model = RecipieIngredient
        row_attrs = {
            "recipie_ingredient_id": lambda record: record.pk
         }
        attrs = {'class': "table table-striped table-hover"}
        fields = {'recipie_ingredient_id', 'recipie_name', 'ingredient',
                  'unit_of_measure', 'value'}
