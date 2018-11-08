from django import forms
from comments.models import Comments
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Comments
		fields = ['user_name', 'body']
