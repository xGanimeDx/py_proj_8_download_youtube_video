from pytube import YouTube
from pytube.cli import on_progress

color = '\033[1;32;32m'
reset_color = '\033[39m'

url = input('Please enter valid YouTube video URL: ')
res_value = ''
while res_value not in ['360', '480', '720', '1080']:
    res_value = input('Please choose the resolution (360, 480, 720, 1080): ')

def download_video(url, res_value):
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    # print(str(yt.length // 60) + ":" + str(yt.length % 60))
    print('\n' + color + 'Downloading: ')
    yt.streams.filter(res=res_value + 'p', progressive=True).first().download()
    print('\nFinished downloading ' + reset_color)

download_video(url, res_value)
