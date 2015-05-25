from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Tweet(models.Model):
	nickname = models.ForeignKey(User, default=True)
	tweet_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=datetime.now, 
									blank=True)

	def __str__(self):
		return self.tweet_text

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username
