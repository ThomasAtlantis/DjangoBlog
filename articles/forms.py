from django import forms
from comments.models import Comments

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['user_name', 'body']