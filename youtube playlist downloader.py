from pytube import Playlist
import os
from os import path

p=Playlist("https://www.youtube.com/playlist?list=PLVPtvlcflR0WwFCeMBMYWgYVwmtonpt8j")

def is_string_in_list(string1,list1):
    for item in list1:
        if string1 in item:
            return True
    return False

if not path.exists(p.title):
    os.makedirs(p.title)

print(f'Downloading: {p.title}')
all_is_not_downloaded=True

while(all_is_not_downloaded):
    try:
        counter=1
        files=os.listdir(f'{p.title}')
        all_videos=[]
        for video in p.videos:
            if not is_string_in_list(video.title,files):
                all_videos.append(video)
        total=len(all_videos)
        for video in all_videos:
            print(f'[{counter}/{total}] {video.title}')
            #video.streams.get_audio_only().download(output_path=f'{p.title}')
            counter+=1
        all_is_not_downloaded=False
        
    except:
        print("Download Failed. Redownloading.")
    

files=os.listdir(f'{p.title}')

files=[ x for x in files if ".mp3" not in x[-4:] ]

total_files=len(files)
counter=1
for file in files:
    print(f'[{counter}/{total}] Converting {file}...')
    full_file_path=f"{p.title}/{file}"
    os.system(f"ffmpeg -i '{full_file_path}' -vn -ac 2 '{full_file_path[:-4]}.mp3'")
    os.remove(full_file_path)
    counter+=1

print("Done. Enjoy. :)")


    



    



