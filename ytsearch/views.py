from django.shortcuts import render
from django.contrib import messages
from pytube import YouTube
from django.http import HttpResponse


from .yts.yt2  import youtube_search, file_path
import json
import time
# Create your views here.


def search(request):
	template = 'ytsearch/index.html'
	print(request.POST)
	if request.POST:
		print("this is what is being sent to youtube " + str(request.POST['search_val']))
		try:
			red = youtube_search(request.POST['search_val'])
		# time.sleep(5)
			# print ([json.loads(i) for i in red[0]])
			context = {
				'videos':[json.loads(i) for i in red[0]],
				'playlist':red[1],
				'channel':red[2],
				'results':len(red[0])
			}
			return render(request, template, context)
		except Exception as e:
			return render(request, template, {'error':"You are not connected to the internet"})
	return render(request, template, {})

def listMedia(request):
	return HttpResponse("media")

def listPlaylist(request):
	return HttpResponse("playlist")

def listChannel(request):
	return HttpResponse("channel")

# def progress_check(stream = None, chunk = None, file_handle = None, remaining = None ):#complete
#     percent = (100*(file_size-remaining))/file_size
#     print("---->> {:00.0f}% downloaded ".format(percent), end="\r")#solve progress 

# def getfile(ids):
# 	try:
# 		url = f'https://www.youtube.com/watch?v={ids}'
# 		video = YouTube(url,on_progress_callback=progress_check)#on_progress_callback=progress_check
# 		vid_type = video.streams.filter(progressive=True, file_extension = "mp4").first()
# 		global file_size
# 		file_size = vid_type.filesize
# 		vid_type.download(file_path())
# 		messages.success(request, 'video downloaded. Check your')
# 	except Exception as e:
# 		if 'url' in str(e):
# 			return HttpResponse("This Video seems to be copyrighted " + str(e))


def download(request):
	if request.POST:
		ids = request.POST['savage']
		getfile(ids)

	return HttpResponse("Wait Your download is starting, you can continue surfing")