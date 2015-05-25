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


class Comment(models.Model):
	tweet = models.ForeignKey(Tweet)
	comment_text = models.CharField(max_length=200)
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.comment_text

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username

'''
 http://www.esotech.org/wp-content/uploads/2011/12/jquery_logo.png
    http://www.linuxtrent.it/sites/default/files/images/drupal-logo.jpg
'''