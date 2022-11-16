from django import forms
from .models import Post

class PostForm(forms.ModelForm):
# We tell Django, PostForm is a ModelForm
    class Meta:
        # 'class Meta', where we tell Django which model should be used to create this form (model=Post)
        model = Post
        fields = ('title', 'text')
        # Finally, we can say which fields should end up in our form.