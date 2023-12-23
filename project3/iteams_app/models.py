from django.db import models

# Create your models here.
class iteams(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()
    image = models.TextField()
    def __str__(self):
        return self.name