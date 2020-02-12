from googleapiclient.discovery import build 
import json
import os


def youtube_search(query, max_results=30): 
	# Arguments that need to passed to the build function 
	DEVELOPER_KEY = "AIzaSyBP1tLKpaLNYBHg8Ymtc5Fp-cI72m9Y1fw"
	YOUTUBE_API_SERVICE_NAME = "youtube"
	YOUTUBE_API_VERSION = "v3"

	# creating Youtube Resource Object 
	youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
											developerKey = DEVELOPER_KEY) 
	
	# calling the search.list method to 
	# retrieve youtube search results 
	search_keyword = youtube_object.search().list(q = query, part = "id, snippet", 
											maxResults = max_results).execute() 
	
	# extracting the results from search response 
	results = search_keyword.get("items", []) 
	# with open("results.txt", "w+") as f:
	# 	json.dump(results, f)

	# empty list to store video, 
	# channel, playlist metadata 
	videos = []	
	playlists = [] 
	vurl = {}
	vl = []
	thumb =[]
	channels = [] 
	
	# extracting required info from each result object 
	for result in results: 
		# video result object 
		if result['id']['kind'] == "youtube#video": 
			videos.append(result["snippet"]["title"])
			thumb.append(result['snippet']['thumbnails']['default']['url'])
			vurl["id"], vurl["name"],vurl["desc"],vurl["thumb"] =result["id"]["videoId"], result["snippet"]["title"], result['snippet']['description'],result['snippet']['thumbnails']['default']['url']
			vl.append(json.dumps(vurl))



			# videos.append("% s % s % s % s)" % (result["snippet"]["title"], 
			# 				result["id"]["videoId"], result['snippet']['description'], 
			# 				result['snippet']['thumbnails']['default']['url'])) 
			# videos["title"], videos["id"],videos["description"] = result["snippet"]["title"], result["id"]["videoId"],result['snippet']['description']
			

		# playlist result object 
		elif result['id']['kind'] == "youtube#playlist": 
			playlists.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
								result["id"]["playlistId"], 
								result['snippet']['description'], 
								result['snippet']['thumbnails']['default']['url'])) 

		# channel result object 
		elif result['id']['kind'] == "youtube#channel": 
			channels.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
								result["id"]["channelId"], 
								result['snippet']['description'], 
								result['snippet']['thumbnails']['default']['url'])) 

	# for i in [json.loads(c) for c in vl]:
	# 	print(i["id"])
	# 	print("\n\n")
	# print(videos)
	return vl,channels, playlists
# 	for key, val in enumerate(videos):
# 		print(f"Videos {key}:{val}") 
# 	print("Channels:\n", "\n".join(channels), "\n") 
# 	print("Playlists:\n", "\n".join(playlists), "\n") 



#show download progress
# def progress_check(stream = None, chunk = None, file_handle = None, remaining = None ,file_size):#complete
#     percent = (100*(file_size-remaining))/file_size
#     print("---->> {:00.0f}% downloaded ".format(percent), end="\r")#solve progress 

#file path to save the video
def file_path():#complete
    home = os.path.expanduser('~')
    dpath = os.path.join(home,'Downloads')
    return dpath

#the download func
# def download(ids):#complete
#     """
#   :Todo
#   		add logic to allow user to choose video quality
#   		and choose conversion to mp3
#                 """
#     url = f'https://www.youtube.com/watch?v={ids}'
#     video = YouTube(url, on_progress_callback=progress_check)
#     vid_type = video.streams.filter(progressive=True, file_extension = "mp4").first()
#     global file_size
#     file_size = vid_type.filesize
#     vid_type.download(file_path())
    # d = input(f"Proceed to download {file_size/1e+6} mb file (y/n) :")
    # if d.lower() == "n":
    #     os.system("clear")
    # elif d.lower() == "y":
    #     vid_type.download(file_path())
    # else:
    #     exit(0)
    #     print("Sorry did not understand command")





if __name__ == "__main__": 
	youtube_search('python', max_results = 10) 
	
