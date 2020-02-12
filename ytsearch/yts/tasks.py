from celery import shared_task
from pytube import YouTube

# def progress_check(stream = None, chunk = None, file_handle = None, remaining = None ):#complete
#     percent = (100*(file_size-remaining))/file_size
#     print("---->> {:00.0f}% downloaded ".format(percent), end="\r")#solve progress 

 
# @shared_task
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

@shared_task
def getfile(ids):
	print(ids)