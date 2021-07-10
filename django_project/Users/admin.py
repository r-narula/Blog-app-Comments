from django.contrib import admin
from .models import (Profile,FormSubmit,UserMetaData,UserTotalHour)
# Register your models here.


list_models = [Profile,FormSubmit,UserTotalHour,UserMetaData]
admin.site.register(list_models)