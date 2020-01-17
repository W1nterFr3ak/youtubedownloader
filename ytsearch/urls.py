from django.urls import path

from .views import (
		search,
		listPlaylist,
		listChannel,
		listMedia,
	)


urlpatterns = [
	path('', search, name='search'),
	path('media/', listMedia,name='media'),
	path('playlist/', listPlaylist, name='playlist'),
	path('channel/', listChannel, name='channel'),
]