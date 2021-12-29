from django.contrib import admin

# Register your models here.

# add RedditBotAccount to admin
from apptest.models import MessageCount, RedditBotAccount

RedditBotAccountAdmin = admin.site.register(RedditBotAccount)
MessageCountob = admin.site.register(MessageCount)
