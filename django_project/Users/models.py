from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from eventSpec.models import Task, Event

# Create your models here.


class Profile(models.Model):
    # fields for it
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpeg", upload_to="profile_pics")
    event_chosen = models.ForeignKey(
        Event, on_delete=models.CASCADE, default=None, blank=True, null=True
    )

    def __str__(self):
        return self.user.username


class FormSubmit(models.Model):
    user_using = models.ForeignKey(User, on_delete=models.CASCADE)
    task_chosen = models.ForeignKey(Task, on_delete=models.CASCADE)
    hours_spent = models.IntegerField(default=0)
    others = models.CharField(max_length=200, blank=True, default="  ")
    image = models.ImageField(default="default.jpeg", upload_to="profile_pics")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_using} on {self.task_chosen}"

    def save(self, *args, **kwargs):
        if self.pk == None:
            ...
        else:
            old_instance = FormSubmit.objects.get(id=self.pk)
            if not old_instance.approved and self.approved:

                query = UserTotalHour.objects.filter(
                    user=self.user_using, event=self.task_chosen.event
                )
                if query.exists():
                    query = query.first()
                    query.hours += self.hours_spent
                    query.save()
                else:
                    UserTotalHour.objects.create(
                        user=self.user_using,
                        event=self.task_chosen.event,
                        hours=self.hours_spent,
                    )

        super(FormSubmit, self).save(*args, **kwargs)

class UserMetaData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_hours = models.IntegerField(default=0)

    def update_hours(self, new_hours):
        self.total_hours += new_hours
        self.save()

    def __str__(self):
        return str(self.user.username)


class UserTotalHour(models.Model):
    # on each project how may hours spent
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    hours = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)
