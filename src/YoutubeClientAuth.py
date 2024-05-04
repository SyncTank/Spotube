import os
from pytube import Playlist, YouTube


def youtube_relog() -> list:
    request_data = []

    return request_data


class YoutubeAuth:
    def __init__(self):
        self.playlist_name: str = ''

    def request_playlist(self, request: str) -> None:
        self.playlist_name = "YoutubeDump.json"
        if os.path.exists(self.playlist_name):
            os.remove(self.playlist_name)

        playlist = Playlist(request)
        playlist_data = set()
        for url in playlist.video_urls:
            youtube = YouTube(url)
            playlist_data.add(youtube.title)
            print(f"Title: {youtube.title}")

        with open("YoutubeDump.txt", "w") as file:
            file.write(str(playlist_data))

    def create_playlist(self, request: str) -> NotImplemented:
        return NotImplemented
