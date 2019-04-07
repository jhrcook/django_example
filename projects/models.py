from django.db import models
from django.contrib import staticfiles
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="static/projects/img",
                              default="website_images/Unknown.png")
    # image = models.FilePathField(path="/projects/img/", default="website_images/Unknown.png")
