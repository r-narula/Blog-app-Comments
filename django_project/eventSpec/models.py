from django.db import models

# Create your models here.

# class MainTable(models.Model):
    # model = models.Char

class BrightSparkEducation(models.Model):
    task = models.CharField(max_length=50,default="None")
    Estimated_total_hours = models.IntegerField(default=0)
    locationOfOperation = models.CharField(max_length=50,default="None")

    def __str__(self):
        return self.task

class Transformers(models.Model):
    task = models.CharField(max_length=50,default="None")
    Estimated_total_hours = models.IntegerField(default=0)
    locationOfOperation = models.CharField(max_length=50,default="None")

    def __str__(self):
        return self.task

class FoodNutrition(models.Model):
    task = models.CharField(max_length=50,default="None")
    Estimated_total_hours = models.IntegerField(default=0)
    locationOfOperation = models.CharField(max_length=50,default="None")

    def __str__(self):
        return self.task

class GenderProgram(models.Model):
    task = models.CharField(max_length=50,default="None")
    Estimated_total_hours = models.IntegerField(default=0)
    locationOfOperation = models.CharField(max_length=50,default="None")

    def __str__(self):
        return self.task

class YoungistaanAnimalHeroes(models.Model):
    task = models.CharField(max_length=50,default="None")
    Estimated_total_hours = models.IntegerField(default=0)
    locationOfOperation = models.CharField(max_length=50,default="None")

    def __str__(self):
        return self.task

class BloodDonor(models.Model):
    task = models.CharField(max_length=50,default="None")
    Estimated_total_hours = models.IntegerField(default=0)
    locationOfOperation = models.CharField(max_length=50,default="None")

    def __str__(self):
        return self.task
