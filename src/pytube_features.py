import os
from pytube import YouTube # type: ignore
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class PytubeDownload():
    def __init__(self, youtube_url, download_path):
        self.youtube_url = youtube_url
        os.chdir(download_path)
        self.yt = YouTube(youtube_url)
        self.filename = self.yt.title

    def download_video(self):
        print(self.youtube_url)
        print('download video...')
        self.yt.streams.filter().get_highest_resolution().download()
        print('Finished!')

    def download_audio(self):
        print(self.youtube_url)
        print('download audio...')
        # 原本取得audio的方法
        # self.yt.streams.filter().get_audio_only().download()
        self.yt.streams.filter(only_audio=True).first().download(
            filename = self.filename + '.mp3'
        )
        print('Finished!')