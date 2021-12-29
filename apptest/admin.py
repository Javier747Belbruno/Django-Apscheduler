from django.contrib import admin

# Register your models here.

# add RedditBotAccount to admin
from apptest.models import RedditBotAccount

RedditBotAccountAdmin = admin.site.register(RedditBotAccount)
