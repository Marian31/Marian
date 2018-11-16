from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from music.forms import UserForm, AlbumForm, SongForm
from music.models import Album, User, Song

# Create your views here.


def method(request):
    form = UserForm(request.POST or None)
    list_user = User.objects.all()
    content = {"list_user": list_user,"form": form}
    if request.method == "POST":
        print(request.POST)
    return render(request, "music/user_site.html", content)


def addUser(request):
    post = QueryDict(request.body)
    User.objects.create(
        first_name=post.get('first_name'),
        mid_name=post.get('mid_name'),
        last_name=post.get('last_name'),
    )
    return HttpResponse("User added")


def deleteUser(request, UserId):
    User.objects.get(pk=int(UserId)).delete()
    return HttpResponse("User deleted")


def userUrl(request, User_name):
    form = AlbumForm(request.POST or None)
    user_name = str(User_name).split()
    for user in User.objects.all():
        if user.mid_name == user_name[0]:
            UserId = user.id
    list_album = []
    for album in Album.objects.all():
        if album.user.id == int(UserId):
            list_album.append(album)
        elif not album.protected:
            m = album
            list_album.append(album)
    content = {"album": list_album}
    if request.method == "POST":
        print(request.POST)
    return render(request, "music\playlist_site.html", locals(), content)


def albumUrl(request, Album_name):
    form = SongForm(request.POST or None)
    list_song = []
    for song in Song.objects.all():
        if song.album.album_title == Album_name:
            list_song.append(song)
    content = {"song": list_song}
    if request.method == "POST":
        print(request.POST)
    return render(request, "music\song_site.html", locals(), content)


def addAlbum(request):
    post = QueryDict(request.body)
    if post.get('protected') == 'on':
        pr = True
    else:
        pr = False
    for user in User.objects.all():
        if str(user.id) == post.get('user'):
            Album.objects.create(
                album_title=post.get('album_title'),
                genre=post.get('genre'),
                protected=pr,
                user=user
            )
            return HttpResponse("Album added")
    return HttpResponse(404)


def deleteAlbum(request, AlbumId):
    Album.objects.get(pk=AlbumId).delete()
    return HttpResponse("Album deleted")


def addSong(request):
    post = QueryDict(request.body)
    for album in Album.objects.all():
        if str(album.id) == post.get('album'):
            Song.objects.create(
                artist=post.get('artist'),
                song_title=post.get('song_title'),
                album=album
            )
            return HttpResponse("Song added")
    return HttpResponse(404)


def deleteSong(request, SongId):
    Song.objects.get(pk=SongId).delete()
    return HttpResponse("Song deleted")