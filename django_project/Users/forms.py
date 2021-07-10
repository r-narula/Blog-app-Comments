from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, FormSubmit, Task


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Model form works with specific db model.
# here we want to update the user profile form hence this thing.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["event_chosen"]

    def save(self):
        super().save()  # saving image first


class CommentForm(forms.ModelForm):
    class Meta:
        model = FormSubmit
        fields = ["task_chosen", "hours_spent", "others", "image"]

    def __init__(self, *args, user=None, location=None, **kwargs):
        print(user)
        super(CommentForm, self).__init__(*args, **kwargs)
        if location is not None:

            self.fields["task_chosen"].queryset = Task.objects.filter(
                event=user.profile.event_chosen, location__iexact=location
            )
        else:
            self.fields["task_chosen"].queryset = Task.objects.filter(
                event=user.profile.event_chosen
            )
