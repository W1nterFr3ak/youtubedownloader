from django.urls import path

from .views import (
		search,
		listPlaylist,
		listChannel,
		listMedia,
		download
	)


urlpatterns = [
	path('', search, name='search'),
	path('media/', listMedia,name='media'),
	path('playlist/', listPlaylist, name='playlist'),
	path('download/', download, name='download'),
	path('channel/', listChannel, name='channel'),
]