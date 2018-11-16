from django.contrib import admin

from music.models import Album, Song, User


admin.site.register(Song)
admin.site.register(Album)
admin.site.register(User)

# Register your models here.
