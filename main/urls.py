from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("<int:id>", views.index, name = "index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path('upd_create', views.Create, name="add"),
    path('view/', views.ViewIngredient, name="view"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("update/<str:pk>", views.update, name="update"),
    path("search_recipe/", views.SearchRecipe, name = "search_recipe"),
    path("update/<recipe_name", views.UpdateRecipe, name = "update_recipe"),
]


urlpatterns += staticfiles_urlpatterns()
