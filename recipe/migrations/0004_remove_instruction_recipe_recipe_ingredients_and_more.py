# Generated by Django 4.2.18 on 2025-02-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_alter_instruction_step_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruction',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default='Ingredients', max_length=100),
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default='Instructions'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Instruction',
        ),
    ]
