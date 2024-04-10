from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100, null=False)
    github = models.URLField(max_length=500, null=False)
    linkedin = models.URLField(max_length=500, null=False)
    bio = models.TextField(null=False)

    def __str__(self):
        return self.name
