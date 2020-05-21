from django.db import models


class Job(models.Model):
    # Job has an image of the job, a summary, and a title
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.title
