from django.contrib import admin
from .models import Profile, FormSubmit, UserMetaData, UserTotalHour

# Register your models here.


list_models = [FormSubmit, UserMetaData]
admin.site.register(list_models)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["event_chosen"]
    list_filter = ["event_chosen"]


@admin.register(UserTotalHour)
class TotalHourAdmin(admin.ModelAdmin):
    list_display = ["event", "user", "hours"]
    list_filter = ["event", "user"]


#     list_display = ["user_using.username", "task_chosen", "hours_spent", "approved"]
# list_filter = ["task_chosen"]
