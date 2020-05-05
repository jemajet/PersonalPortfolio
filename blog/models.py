from django.db import models


class Blog(models.Model):
    # Blog has a title, a publication date, an image, and a body
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
