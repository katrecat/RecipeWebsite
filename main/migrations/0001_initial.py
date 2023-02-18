# Generated by Django 4.1.6 on 2023-02-13 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_name', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipie',
            fields=[
                ('recipie_name', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(max_length=200)),
                ('category_name', models.ManyToManyField(blank=True, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='RecipieIngredient',
            fields=[
                ('recipie_ingredient_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('unit_of_measure', models.CharField(max_length=20, unique=True)),
                ('value', models.FloatField()),
                ('ingredient_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ingredient')),
                ('recipie_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.recipie')),
            ],
        ),
    ]