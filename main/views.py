from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ingredient, Category, RecipieIngredient, Recipie
from .forms import IngredientForm, RecepieIngredientForm, CategoryForm, RecipieForm
from .tables import IngredientTable, CategoryTable, RecipieIngredientTable, RecipieTable

# Create your views here.
def index(response, id):
    ls = Ingredient.objects.get(ingredient_id=id)
    #return HttpResponse("<h1>%s</h1>" % ls.name)
    return render(response, "main/view.html", {"ls":ls})


def home(response):
    return render(response, "main/home.html", {})

#-------------------Ingredient-------------------------


def Create(response):
    form1 = IngredientForm()
    if response.method == "POST":
        print('Printing POST :', response.POST)
        form1 = IngredientForm(response.POST)
        if form1.is_valid():
            form1.save()
            print("33333333333333333")
        if form1.has_changed():
            print("000000000000000000000000")
        else:
            print("11111111111111111111") #when we write not in this field


    form2 = CategoryForm()
    if response.method == "POST":
        print('Printing POST :', response.POST)
        form2 = CategoryForm(response.POST)
        if form2.is_valid():
            form2.save()

    form3 = RecipieForm()
    if response.method == "POST":
        print('Printing POST :', response.POST)
        form3 = RecipieForm(response.POST)
        if form3.is_valid():
            form3.save()

    form4 = RecepieIngredientForm()
    if response.method == "POST":
        print('Printing POST :', response.POST)
        form4 = RecepieIngredientForm(response.POST)
        if form4.is_valid():
            form4.save()
    contex = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4}


    return  render(response, 'main/upd_create.html', contex)


def ViewIngredient(response):
    table1 = IngredientTable(Ingredient.objects.all())
    table2 = CategoryTable(Category.objects.all())
    table3 = RecipieIngredientTable(RecipieIngredient.objects.all())
    table4 = RecipieTable(Recipie.objects.all())
    return render(response, "main/view.html", {"table1": table1,"table2": table2,"table3": table3,"table4": table4})
'''
def DeleteRecipieIngredient(response,pk):
    recipieingredient = RecipieIngredient.objects.get(recipie_ingredient_id=pk)
    if response.method == "POST":
        recipieingredient.delete()
        return redirect("/view")

    contex = {"item":recipieingredient}

    return render(response,"main/delete.html", contex)
'''

def SearchRecipe(response):
    if response.method == "POST":
        searched = response.POST['searched']
        recipes = Recipie.objects.filter(recipie_name__contains=searched)

        return render(response, 'main/search_recipe.html', {'searched':searched, 'recipes':recipes})
    else:
        return render(response, 'main/search_recipe.html', {})

def UpdateRecipe(response, recipe_name):
    recipe = Recipie.objects.get(pk=recipe_name)
    return render(response, 'main/update.html', {'recipe':recipe})
    stadium = Stadium.objects.get(stadium_id=pk)
    form = StadiumForm(instance=stadium)
    contex = {'form':form}

    if response.method == "POST":
         form = StadiumForm(response.POST, instance=stadium)
         if form.is_valid():
             form.save()
             return redirect('/stadium_list/0' )

    return  render(response, 'master/stadium_form.html', contex)
