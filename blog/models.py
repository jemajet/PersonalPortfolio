from django.db import models


class Blog(models.Model):
    # Blog has a title, a publication date, an image, and a body
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        if len(self.body) < 100:
            return self.body
        else:
            return self.body[:100] + "... Read More"

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")

    def __str__(self):
        return self.title
