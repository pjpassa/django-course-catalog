from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField(choices=[(2, "2 Weeks"), (8, "8 Weeks")])
    courseArt = models.ImageField()

    def __str__(self):
        return "{}: {}".format(self.title, self.instructor)
