from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.name} - {self.credits}"


class Student(models.Model):
    name = models.CharField(max_length=200)
    sem = models.IntegerField()
    courses = models.ManyToManyField(Course,related_name='students') 
    # related_name defines the name you use to access the reverse relationship from the related model.

    def __str__(self):
        return f"{self.id} - {self.name}"