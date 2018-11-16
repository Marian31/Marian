"""Playlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.method, name="method"),

    path('user/add', views.addUser, name="AddUser"),
    path('user/<User_name>', views.userUrl, name="userUrl"),
    path('u/<UserId>', views.deleteUser, name="deleteUser"),

    path('user/album/add', views.addAlbum, name="AddAlbum"),
    path('album/<Album_name>', views.albumUrl, name="albumUrl"),
    path('user/a/<AlbumId>', views.deleteAlbum, name="deleteAlbum"),

    path('album/song/add', views.addSong, name="AddSong"),
    path('album/s/<SongId>', views.deleteSong, name="deleteSong"),

]
