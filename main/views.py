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

# -------------------Ingredient-------------------------


def Create(response):
    form1 = IngredientForm()
    form2 = CategoryForm()
    form3 = RecipieForm()
    form4 = RecepieIngredientForm()

    if response.method == "POST":
        print('Printing POST :', response.POST)
        if 'submit-ingredient' in response.POST:
            form1 = IngredientForm(response.POST)
            if form1.has_changed() and form1.is_valid():
                print("Form1 is valid and changed, saving")
                form1.save()

        elif 'submit-category' in response.POST:
            form2 = CategoryForm(response.POST)
            if form2.is_valid() and form2.has_changed():
                print("Form2 is valid and changed, saving")
                form2.save()

        elif 'submit-recipe' in response.POST:
            form3 = RecipieForm(response.POST)
            if form3.is_valid() and form3.has_changed():
                print("Form3 is valid and changed, saving")
                form3.save()

        elif 'submit-ingredient-in-recipe' in response.POST:
            form4 = RecepieIngredientForm(response.POST)
            if form4.is_valid() and form4.has_changed():
                print("Form4 is valid and changed, saving")
                form4.save()

    contex = {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4}

    return render(response, 'main/upd_create.html', contex)


def ViewIngredient(response):
    print(response.method)
    if response.method == "GET" and 'sort' in response.GET:
        key = response.GET['sort']
        table_3_keys = ["recipie_name", "value", "ingredient",
                        "recipie_ingredient_id", "unit_of_measure"]
        table_4_keys = ["description", "recipie_name"]
        if key == 'ingredient_name':
            table1 = IngredientTable(Ingredient.objects.order_by(key))
        else:
            table1 = IngredientTable(Ingredient.objects.all())
        if key == 'category_name':
            table2 = CategoryTable(Category.objects.order_by(key))
        else:
            table2 = CategoryTable(Category.objects.all())
        if key in table_3_keys:
            table3 = RecipieIngredientTable(RecipieIngredient.objects.order_by(key))    # noqa: E501
        else:
            table3 = RecipieIngredientTable(RecipieIngredient.objects.all())
        if key in table_4_keys:
            print("key in table_4_keys")
            table4 = RecipieTable(Recipie.objects.order_by(key))
        else:
            table4 = RecipieTable(Recipie.objects.all())
    else:
        table1 = IngredientTable(Ingredient.objects.all())
        table2 = CategoryTable(Category.objects.all())
        table3 = RecipieIngredientTable(RecipieIngredient.objects.all())
        table4 = RecipieTable(Recipie.objects.all())
    return render(response, "main/view.html", {"table1": table1,
                                               "table2": table2,
                                               "table3": table3,
                                               "table4": table4})


def delete(request, pk):
    if request.method == "POST":
        recipe = Recipie.objects.get(pk=pk)
        recipe.delete()
        return redirect('/view/')
    context = {'item': pk}
    return render(request, 'main/delete.html', context)


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
