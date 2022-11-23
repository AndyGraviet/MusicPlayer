from django.db import models

# Create your models here.

# create a model to store the song information

class Song(models.Model):
    title= models.CharField(max_length= 100)
    artist= models.CharField(max_length= 50)
    image= models.ImageField()
    audio_file= models.FileField(blank=True, null=True)
    duration = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title

    