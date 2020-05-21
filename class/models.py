from django.db import models

# Create your models here.


class Class(models.Model):
        # Job has an image of the job, a summary, and a title
    title = models.CharField(max_length=200)
    class_year = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()

    def short_summary(self):
        max_words = 25
        if len(self.summary.split(" ")) < max_words:
            return self.summary
        else:
            return " ".join(self.summary.split(" ")[:max_words]) + "... Read More"

    def __str__(self):
        return self.title
