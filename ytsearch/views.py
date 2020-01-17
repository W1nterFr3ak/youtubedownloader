from django.shortcuts import render
from django.http import HttpResponse
from .yts.yt2  import youtube_search
import time
# Create your views here.


def search(request):
	template = 'ytsearch/base.html'
	if request.POST:
		print(request.POST['search_val'])
		red = youtube_search(request.POST['search_val'])
	# time.sleep(5)
		context = {
			'videos':red[0],
			'playlist':red[1],
			'channel':red[2],
			'thumb':red[3],
			'results':len(red[0])
		}
		return render(request, template, context)
	return render(request, template, {})
def listMedia(request):
	return HttpResponse("media")

def listPlaylist(request):
	return HttpResponse("playlist")

def listChannel(request):
	return HttpResponse("channel")