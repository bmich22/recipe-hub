from django.contrib import admin
from .models import Recipe


# # ✅ Step 1: Create an InlineAdmin for Ingredients
# class IngredientInline(admin.TabularInline):  # or admin.StackedInline for a different layout
#     model = Ingredient
#     extra = 0  # Allows adding 3 ingredients by default


# # ✅ Step 1.5: Create an InlineAdmin for Instructions
# class InstructionInline(admin.TabularInline):  # or admin.StackedInline for a different layout
#     model = Instruction
#     extra = 0  # Allows adding 3 instructions by default


# # ✅ Step 2: Register RecipeAdmin with the inline Ingredient form
# @admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status', 'created_on')
#     prepopulated_fields = {'slug': ('title',)}  # Auto-fills slug from title
#     inlines = [IngredientInline, InstructionInline]  # ✅ Includes Ingredient form inside Recipe


# # ✅ Step 3: Register Ingredient separately (optional)
# # @admin.register(Ingredient)
# # class IngredientAdmin(admin.ModelAdmin):
# #     list_display = ('recipe', 'name', 'amount', 'unit')



