from django.db import models

# Create your models here.
class userinfo(models.Model):
    name = models.CharField(max_length=50)
    life = models.TextField()
    def __str__(self):
        return self.name
