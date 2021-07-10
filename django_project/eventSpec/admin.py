from django.contrib import admin
from .models import (BloodDonor,YoungistaanAnimalHeroes,GenderProgram,
                FoodNutrition,BrightSparkEducation,Transformers)
# Register your models here.

models_list = [BloodDonor,YoungistaanAnimalHeroes,GenderProgram,
                FoodNutrition,BrightSparkEducation,Transformers]

admin.site.register(models_list)

