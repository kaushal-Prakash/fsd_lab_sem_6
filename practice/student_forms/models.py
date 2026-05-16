from django.db import models

class Project(models.Model):
    topic = models.CharField(max_length=100)
    languages_used = models.TextField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.topic
