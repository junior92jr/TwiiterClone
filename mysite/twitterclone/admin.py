from django.contrib import admin
from twitterclone.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['tweet_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Tweet, TweetAdmin)