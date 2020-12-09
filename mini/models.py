from django.db import models

# Create your models here.


class Post(models.Model):
    body = models.CharField(max_length=300)
    author = models.CharField(max_length=40)

    def __str__(self):
        return self.body
        