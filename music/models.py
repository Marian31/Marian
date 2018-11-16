from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    mid_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.mid_name} {self.first_name} {self.last_name}'


class Album(models.Model):
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    protected = models.BooleanField(default=True)
    user = models.ForeignKey(User, related_name="albums", on_delete=models.CASCADE)

    def __str__(self):
        return self.album_title


class Song(models.Model):
    song_title = models.CharField ( max_length=255 )
    artist = models.CharField(max_length=255)
    album = models.ForeignKey(Album, related_name="songs", on_delete=models.CASCADE)

    def __str__(self):
        return self.song_title

# Create your models here.
