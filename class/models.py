from django.db import models

# Create your models here.


class Class(models.Model):
        # Job has an image of the job, a summary, and a title
    title = models.CharField(max_length=200)
    class_year = models.CharField(max_length=200)
    class_description = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return self.title
