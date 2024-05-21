import os
from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class PytubeDownload():
    def __init__(self, youtube_url, download_path, progressObj):
        self.youtube_url = youtube_url
        os.chdir(download_path)
        self.progressObj = progressObj
        self.yt = YouTube(youtube_url, on_progress_callback=self.onProgress)
        self.filename = self.yt.title

    def onProgress(self, stream, chunk, remains):
        total = stream.filesize
        percent = (total-remains) / total * 100
        self.progressObj.setValue(int(percent))

    def download_video(self):
        self.yt.streams.filter().get_highest_resolution().download()

    def download_audio(self):
        # 原本取得audio的方法
        # self.yt.streams.filter().get_audio_only().download()
        self.yt.streams.filter(only_audio=True).first().download(filename = self.filename + '.mp3')