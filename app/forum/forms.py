from django import forms
from martor.fields import MartorFormField
from . import models


class PostForm(forms.ModelForm):
    content = MartorFormField()

    class Meta:
        model = models.ForumPost
        fields = ["title", "content"]

