from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from eventSpec.models import BrightSparkEducation,GenderProgram
# Create your models here.

class Profile(models.Model):
    # fields for it
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpeg',upload_to='profile_pics')

    def __str__(self):
        return self.user.username 

# class Task(models.Model):
#     task = models.CharField(max_length=50,default="None")
#     Total_hours_done = models.IntegerField(default=0)

#     def __str__(self):
#         return self.task

class FormSubmit(models.Model):
    user_using = models.ForeignKey(User,on_delete=models.CASCADE)
    task_choosen = models.ForeignKey(BrightSparkEducation,on_delete=models.CASCADE)
    hours_spent = models.IntegerField(default=0)
    others = models.CharField(max_length=200,blank=True,default="  ")
    image = models.ImageField(default="default.jpeg",upload_to='profile_pics')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_using} on {self.task_choosen}'

    def save(self, *args, **kwargs):
        if self.pk==None:
            UserMetaData.objects.get(user=self.user_using).update_hours(self.hours_spent)
        super(FormSubmit, self).save(*args, **kwargs)

class UserMetaData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_hours = models.IntegerField(default=0)

    def update_hours(self,new_hours):
        self.total_hours += new_hours
        self.save()

    def __str__(self):
        return str(self.user.username)

class UserTotalHour(models.Model):
    # on each project how may hours spent 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    BrightSparkEducation = models.IntegerField(default=0)
    Transformers = models.IntegerField(default=0)
    FoodNutrition = models.IntegerField(default=0)
    GenderProgram = models.IntegerField(default=0)
    YoungistaanAnimalHeroes = models.IntegerField(default=0)
    BloodDonor = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)