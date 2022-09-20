from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=125)
    published = models.DateTimeField()
    audio = models.URLField()
    guid = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.podcast_name}: {self.title}"