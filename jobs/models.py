from django.db import models


class Job(models.Model):
    # Job has an image of the job and a summary
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
