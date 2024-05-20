import pytube_features

youtube_url = 'https://www.youtube.com/watch?v=Y8JFxS1HlDo&ab_channel=STARSHIP'
download_path = 'C:/Users/arif1/Downloads'

pyt = pytube_features.PytubeDownload(youtube_url, download_path)
pyt.download_video()