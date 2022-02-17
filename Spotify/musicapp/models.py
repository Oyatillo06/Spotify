from django.db import models

class Artis(models.Model):
    name=models.CharField(max_length=30)
    yonalish=models.CharField(max_length=20,blank=True)
    description=models.TextField()
    image=models.URLField(blank=True)
    def __str__(self):
        return self.name
class Album(models.Model):
    title=models.CharField(max_length=20)
    date=models.DateField()
    cover=models.URLField(blank=True)
    artist=models.ForeignKey(Artis,on_delete=models.CASCADE,related_name="album_songs")

    def __str__(self):
        return self.title
class Song(models.Model):
    title=models.CharField(max_length=20)
    cover=models.URLField(blank=True)
    lyrics=models.TextField(blank=True)
    duration=models.DurationField()
    sourse=models.URLField(blank=True)
    albom=models.ForeignKey(Album,on_delete=models.CASCADE)
    eshitildi=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.title,self.cover}"

