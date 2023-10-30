from django.db import models

# Create your models here.


class Class(models.Model):
        # Job has an image of the job, a summary, and a title
    title = models.CharField(max_length=200)
    class_year = models.CharField(max_length=200)
    class_description = models.TextField()
    summary = models.TextField()

    @staticmethod
    def course_6_classes(classes):
        course_6 = []
        non_course_6 = []
        for c in classes:
            if "6." in c.title:
                course_6.append(c)
            else:
                non_course_6.append(c)
        return course_6, non_course_6

    def __str__(self):
        return self.title
