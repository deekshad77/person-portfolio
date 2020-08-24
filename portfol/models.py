from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100)
    discription=models.CharField(max_length=200)
    image=models.ImageField(upload_to='portfol/images/')
    url=models.URLField(blank=True)

    def __str__(self):
        return self.title