from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ['your_name','comment']
        fields = ["comment"]

    def __str__(self):
        return f"{self.comment} by {self.your_name}"