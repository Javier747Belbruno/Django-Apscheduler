from django.db import models

# Create your models here.

# reddit bot account API
class RedditBotAccount(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (
            self.username
            + " "
            + self.password
            + " "
            + self.client_id
            + " "
            + self.client_secret
            + " "
            + self.user_agent
        )
