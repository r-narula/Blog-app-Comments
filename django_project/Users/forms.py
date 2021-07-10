from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,FormSubmit

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

# Model form works with specific db model.
# here we want to update the user profile form hence this thing.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    def save(self):
        super().save()  # saving image first

class CommentForm(forms.ModelForm):
    class Meta:
        model = FormSubmit
        fields = ["task_choosen","hours_spent","others","image"]