# Generated by Django 4.2.18 on 2025-02-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_remove_instruction_recipe_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='Ingredients'),
        ),
    ]
