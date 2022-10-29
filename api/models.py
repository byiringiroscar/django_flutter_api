from django.db import models


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=250, default="oscar neon")
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated']
