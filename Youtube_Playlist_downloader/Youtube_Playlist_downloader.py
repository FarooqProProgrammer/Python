from pytube import Playlist
link=input("Enter Playlist Link ")
pt=Playlist(link)
print("---------------------------------------------------------------")
print(f'Downloading: {pt.title}')
print("---------------------------------------------------------------")
s=1
for video in pt.videos:
    print("---------------------------------------------------------------")
    print(f'{s}: {video.title}')
    print("---------------------------------------------------------------")
    video.streams.filter(res="360p").first().download()
print("Download Ending")
