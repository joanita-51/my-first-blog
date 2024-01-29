from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'photo', 'ingredients_list', 'instructions', 'cooking_tips', 'categories', 'cooking_demonstration_video')