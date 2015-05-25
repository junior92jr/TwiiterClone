from django.contrib import admin
from twitterclone.models import Tweet, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['tweet_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [CommentInline]

admin.site.register(Tweet, TweetAdmin)