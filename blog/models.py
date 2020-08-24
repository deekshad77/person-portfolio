from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    discription = models.TextField(max_length=1000)

    def __str__(self):
        return "Title" + self.title


