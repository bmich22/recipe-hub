# Generated by Django 4.2.18 on 2025-02-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='step_number',
            field=models.CharField(max_length=2),
        ),
    ]
