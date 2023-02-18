#python manage.py makemigrations main
#python manage.py migrate


#python manage.py shell
#from main.models import Item, ToOoList
#t=ToDoList(name="Tims List")
#t.save()
#ToDoList.objects.all()
#ToDoList.objects.get(id=1)
#t.item_set.create(text="Go to mall", complete=False)
#t.filter(name__startswith="Tim")

#del_object = t.get(id=1)
#del_object.delete()

#python manage.py createsuperuser
from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    #ingredient_id = models.AutoField(primary_key=True,unique=True)
    ingredient_name = models.CharField(primary_key=True, max_length=20, unique=True)
    def __str__(self):
        return str(self.ingredient_name)

class Category(models.Model):
    category_name = models.CharField(primary_key=True, max_length=20, unique=True)
    def __str__(self):
        return str(self.category_name)


class Recipie(models.Model):
    recipie_name = models.CharField(primary_key=True, max_length=20, unique=True)
    category_name = models.ManyToManyField(Category, blank=True)
    description = models.TextField(max_length=200)
    def __str__(self):
        return str(self.recipie_name)

    def get_absolute_url(self):
        return reverse('search_recipe')

class RecipieIngredient(models.Model):
    recipie_ingredient_id = models.AutoField(primary_key=True, unique=True)
    recipie_name = models.ForeignKey(Recipie, on_delete=models.CASCADE, null=True)
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    unit_of_measure = models.CharField(max_length=20, unique=True)
    value = models.FloatField()
    def __str__(self):
        return str(self.recipie_ingredient_id)



