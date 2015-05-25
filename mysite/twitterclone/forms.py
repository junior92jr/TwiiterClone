from django import forms
from django.contrib.auth.models import User
from twitterclone.models import Tweet, Comment, UserProfile

class TweetForm(forms.ModelForm):
	tweet_text = forms.CharField(max_length=200, 
						help_text='Enter your Tweet.')

	class Meta:
		model = Tweet
		fields = ('tweet_text',)
		exclude= ('nickname',)


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
