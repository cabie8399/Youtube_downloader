import os
from pytube import YouTube # type: ignore
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class PytubeDownload():
    def __init__(self, youtube_url, download_path):
        self.youtube_url = youtube_url
        os.chdir(download_path)
        self.yt = YouTube(youtube_url)

    def download_video(self):
        print('download video...')
        self.yt.streams.filter().get_highest_resolution().download()
        print('Finished!')

    def download_audio(self):
        print('download audio...')
        self.yt.streams.filter().get_audio_only().download()
        print('Finished!')